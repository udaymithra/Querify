from flask import Blueprint,render_template,request,redirect,url_for
from flask_login import login_required,current_user
from .models import Post,Likes,Comments,Reply,CommentsLike
from .import db
import datetime
from pytz import timezone
from .models import User,get_user_id
views=Blueprint('views',__name__)
from sqlalchemy import func

def get_likes_count(all_posts):
    
    likesCount=[]
    for post in all_posts:
        likeCount=Likes.query.filter_by(postId=post.id).count()
        likesCount.append(likeCount)
    return likesCount    

def likes_count_by_id(postId):
    likeCount=Likes.query.filter_by(postId=postId).count()
    return likeCount
def update_count_by_id(postId):
    new_like_rec=Likes(postId=postId)
    db.session.add(new_like_rec)
    db.session.commit()
def delete_count_by_id(postId):
    user_id = get_user_id()  
    record = Likes.query.filter_by(postId=postId, userId=user_id).first()

    if record and record.userId == user_id:
        # Only delete if the record exists and belongs to the current user
        db.session.delete(record)
        db.session.commit()
        return True  # Indicate successful deletion (optional)
    else:
        return False  #

def get_user_info(fetchRequest):

    all_posts=Post.query.all() if fetchRequest=='all' else Post.query.filter_by(id=fetchRequest)
    userPostInfo=[]
    likesCount=get_likes_count(all_posts)
    index=0
    for post in all_posts:
       
        user=User.query.filter_by(id=post.userId).first()
        user_id = get_user_id()  
        record = Likes.query.filter_by(postId=post.id, userId=user_id).first()
        record = True if record else False
        userObject={'userFullName':user.firstName+" "+user.lastName,'postedDate':"-".join(str(post.date)[0:10].split('-')[::-1]),'postLikes':likesCount[index],'postId':post.id,'postLiked':record}
        userPostInfo.append(userObject)
        index+=1
    return [userPostInfo,all_posts]

def get_comments_by_post_id(postId):
    commentsInfo=Comments.query.filter_by(postId=postId).all()
    userId=get_user_id()
    commentLikedList=[]
    commentsLikedCount=dict()
    for comment in commentsInfo:
        commentLiked = CommentsLike.query.filter_by(commentId=comment.id, userId=userId).count()
        if commentLiked:
            commentLikedList.append(1)
        else:
            commentLikedList.append(0)
        commentLikeCount=CommentsLike.query.filter_by(commentId=comment.id).count()
        commentsLikedCount[comment.id]=commentLikeCount


    return [commentsInfo,commentLikedList,commentsLikedCount]



def get_replies_to_comments_by_post_id(postId):
    repliesInfo=dict()
    commentsList=Comments.query.filter_by(postId=postId).all()
    for comment in commentsList:
        repliesList=Reply.query.filter_by(commentId=comment.id).all()
        repliesInfo[comment.id]=repliesList if repliesList else []
    return repliesInfo
def get_user_name_by_user_id(userId):

    user=User.query.filter_by(id=userId).first()
    
    return user.firstName+" "+user.lastName 
def getCommentedByList(postId):
    commentedBy=[]
    commentsList=Comments.query.filter_by(postId=postId).all()
    for comment in commentsList:
        user=User.query.filter_by(id=comment.userId).first()
        commentedBy.append(user.firstName+" "+user.lastName)
    return commentedBy

'''
 Realtime Like and Dislike Count of Comments!

'''
def like_count_of_comment_by_id(userId,commentId):
    commentLikeCount=CommentsLike.query.filter_by(commentId=commentId).count()
    print("commentLikes",commentLikeCount)
    return commentLikeCount
def update_comment_count_by_id(userId,commentId):
    new_record=CommentsLike(commentId=commentId,userId=userId)
    db.session.add(new_record)
    db.session.commit()

def delete_comment_count_by_id(userId,commentId):
    record = CommentsLike.query.filter_by(commentId=commentId,userId=userId).first()
    print("In delete section func")
    if record:
        # Only delete if the record exists and belongs to the current user
        db.session.delete(record)
        print('removed the count')
        db.session.commit()
        return True  # Indicate successful deletion (optional)
    else:
        return False  #

    

''' Profile Section Infor Functions'''
def get_user_details(userId):

    user=User.query.filter_by(id=userId).first()

    userDetails=dict()
    userDetails['userId']=userId
    userDetails['firstName']=user.firstName
    userDetails['lastName']=user.lastName
    userDetails['emailAddress']=user.emailAddress
    userDetails['posts']=[]
    
    posts=Post.query.filter_by(userId=userId).all()
    for post in posts:
        postDetails={}
        postDetails['postId']=post.id
        postDetails['postTitle']=post.title
        postDetails['postContent']=post.content
        userDetails['posts'].append(postDetails)
    
   
    return userDetails








@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'GET':
        userPostInfo,all_posts =get_user_info('all')
        return render_template('Home.html', all_posts=all_posts[::-1],users=userPostInfo[::-1], postCategory=True)
    else:

        serverMessage=request.args.get('message')
        serverCategory=request.args.get('category')
    
        return render_template('Home.html',message=serverMessage, category=serverCategory)
'''
Deletes all functionality (Temp)
'''
def delete_all_posts():
    # Delete all posts using query.delete()
    db.session.query(Post).delete()

    # Commit the changes to the database
    db.session.commit()
    print("All posts deleted successfully!")
def delete_all_comments():
    db.session.query(Comments).delete()
    db.session.commit()
    print("All COmments deleted")

def delete_all_replies():
    db.session.query(Reply).delete()
    db.session.commit()
    print("All replies deleted successfully!")
'''Delete all ends here '''
@views.route('/post', methods=['POST','GET'])
@login_required
def post():
    print("In post call")
    if request.method == 'POST':
        data=request.form
        title=data.get('title')
        editorContent=data.get('editor')
        now_utc = datetime.datetime.utcnow()
        # Convert UTC time to user's region time zone
        user_tz = timezone('Asia/Kolkata')
        now_user_region = now_utc.astimezone(user_tz)
        new_post=Post(userId=current_user.id, title=title,content=editorContent,date=now_user_region)
        db.session.add(new_post)
        db.session.commit()
        # delete_all_posts()

        
        return redirect(url_for('views.home',message="Post Successful", category=True ))
    return render_template('Post.html')

@views.route('/comment/<int:post_id>', methods=['POST','GET'])
@login_required
def comment(post_id):
    #delete_all_comments()
    userPostInfo,postDetails=get_user_info(post_id)
    userPostInfo[0]['postLikes']=likes_count_by_id(post_id)
    commentsInfo,commentLikedList,commentsLikedCount=get_comments_by_post_id(post_id)
    repliesInfo=get_replies_to_comments_by_post_id(post_id)
    userCommentedByList=getCommentedByList(post_id)
    if request.method == 'POST':
        data=request.form
        postId=userPostInfo[0]['postId']
        userId=get_user_id()
        userName=get_user_name_by_user_id(userId).lower()
        commentContent=data.get('comment')
        now_utc = datetime.datetime.utcnow()
        # Convert UTC time to user's region time zone
        user_tz = timezone('Asia/Kolkata')
        now_user_region = now_utc.astimezone(user_tz)
        new_comment=Comments(userId=userId,postId=postId,content=commentContent,date=now_user_region)
        db.session.add(new_comment)
        db.session.commit()
        # delete_all_comments()
        commentsInfo,commentLikedList,commentsLikedCount=get_comments_by_post_id(postId)
        userCommentedByList=getCommentedByList(postId)
        return render_template('Comment.html',userPostInfo=userPostInfo[0],postDetails=postDetails.first(),commentsList=commentsInfo[::-1],commentedByList=userCommentedByList[::-1],lengthComments=len(userCommentedByList),commentLikedList=commentLikedList[::-1],commentsLikedCount=commentsLikedCount,repliesInfo=repliesInfo,lengthReplies=len(repliesInfo))

    
    return render_template('Comment.html',userPostInfo=userPostInfo[0],postDetails=postDetails.first(),commentsList=commentsInfo[::-1],commentedByList=userCommentedByList[::-1],lengthComments=len(userCommentedByList),commentLikedList=commentLikedList[::-1],commentsLikedCount=commentsLikedCount,repliesInfo=repliesInfo,lengthReplies=len(repliesInfo))



@views.route('/comment/reply/<int:comment_id>', methods=['POST'])
@login_required

def reply(comment_id):


    if request.method == 'POST':
        data=request.form
        repliedTo=data.get('replyTo')
        postId=data.get('postId')
        commentId=comment_id
        replyContent=data.get('replyContent')
        userId=get_user_id()
        userName=get_user_name_by_user_id(userId).lower()
        now_utc = datetime.datetime.utcnow()
        # Convert UTC time to user's region time zone
        user_tz = timezone('Asia/Kolkata')
        date = now_utc.astimezone(user_tz)
        new_reply=Reply(commentId=commentId,content=replyContent,date=date,repliedBy=userName,repliedTo=repliedTo,postId=postId,userId=userId)
        db.session.add(new_reply)
        db.session.commit()
        return redirect(url_for('views.comment',post_id=postId))
    #delete_all_replies()
    return 'Replying to {}'.format(comment_id)
@views.route('/delete/comment', methods=['POST'])
@login_required
def deleteComment():

    if request.method == 'POST':
        data=request.form
        commentId=data.get('commentId')
        postId=data.get('postId')
        commentRec=Comments.query.get(commentId)
        if not commentRec:
            return "Comment not found.", 404
        db.session.delete(commentRec)
        db.session.commit()
        return redirect("/comment/{}".format(postId))

    else:
        return '404 Error', 404

@views.route('/delete/reply', methods=['POST'])
@login_required
def deleteReply():

    if request.method == 'POST':
        data=request.form
        replyId=data.get('replyId')
        postId=data.get('postId')
        replyRec=Reply.query.get(replyId)
        if not replyRec:
            return "Comment not found.", 404
        db.session.delete(replyRec)
        db.session.commit()
        return redirect("/comment/{}".format(postId))

    else:
        return '404 Error', 404

@views.route('/profile', methods=['GET', 'POST'])
@login_required
def Profile():

    userId=get_user_id()
    userDetails=get_user_details(userId)
    if request.method=='POST':
        data=request.form
        firstName=data.get('firstName')
        lastName=data.get('lastName')
        user=User.query.get(userId)
        if user:
            user.firstName=firstName
            user.lastName=lastName
            db.session.commit()
        userDetails=get_user_details(userId)
        return render_template('Profile.html',userDetails=userDetails, userPosts=userDetails['posts'] , postsCount=len(userDetails['posts']))
        
   
    return render_template('Profile.html',userDetails=userDetails, userPosts=userDetails['posts'] , postsCount=len(userDetails['posts']))

@views.route('/delete', methods=['POST'])
@login_required
def delete():
    
    data=request.form
    postId=data.get('postId')
    postRec=Post.query.get(postId)
    if not postRec:
        return "Post not found.", 404
    db.session.delete(postRec)
    db.session.commit()
    
    return redirect('/profile')

@views.route('/search', methods=['POST'])
@login_required
def search():
    if request.method == 'POST':
        data=request.form
        searchQuery=data.get('search')
        
        userPostInfo,all_posts =get_user_info('all')
        filtered_posts=[]
        filteredPostInfo=[]

        for post in all_posts:
            if searchQuery.lower() in post.title.lower() or searchQuery in post.content.lower():
                filtered_posts.append(post)
            index=0
        likesCount=get_likes_count(filtered_posts)

        
        for post in filtered_posts:
       
            user=User.query.filter_by(id=post.userId).first()
            user_id = get_user_id()  
            record = Likes.query.filter_by(postId=post.id, userId=user_id).first()
            record = True if record else False
            userObject={'userFullName':user.firstName+" "+user.lastName,'postedDate':"-".join(str(post.date)[0:10].split('-')[::-1]),'postLikes':likesCount[index],'postId':post.id,'postLiked':record}
            filteredPostInfo.append(userObject)
            index+=1
            
        return render_template('Home.html', all_posts=filtered_posts,users=filteredPostInfo, postCategory=True)
    else:
        return '404 Not Found',404