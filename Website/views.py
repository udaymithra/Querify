from flask import Blueprint,render_template,request,redirect,url_for
from flask_login import login_required,current_user
from .models import Post,Likes,Comments
from .import db
import datetime
from pytz import timezone
from .models import User,get_user_id
views=Blueprint('views',__name__)
from sqlalchemy import func

def get_likes_count():
    all_posts=Post.query.all()
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
    likesCount=get_likes_count()
    print("likesCount", likesCount)
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
    return commentsInfo
def get_user_name_by_user_id(userId):

    user=User.query.filter_by(id=userId).first()
    print('userC')
    print(user.firstName+" "+user.lastName)
    return user.firstName+" "+user.lastName 
def getCommentedByList(postId):
    commentedBy=[]
    commentsList=Comments.query.filter_by(postId=postId).all()
    for comment in commentsList:
        user=User.query.filter_by(id=comment.userId).first()
        commentedBy.append(user.firstName+" "+user.lastName)
    return commentedBy

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
    print(userPostInfo)
    print(postDetails.first().id)
    commentsInfo=get_comments_by_post_id(post_id)
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
        commentsInfo=get_comments_by_post_id(postId)
        userCommentedByList=getCommentedByList(postId)
        print(commentsInfo)
        return render_template('Comment.html',userPostInfo=userPostInfo[0],postDetails=postDetails.first(),commentsList=commentsInfo[::-1],commentedByList=userCommentedByList[::-1],lengthComments=len(userCommentedByList))


    return render_template('Comment.html',userPostInfo=userPostInfo[0],postDetails=postDetails.first(),commentsList=commentsInfo[::-1],commentedByList=userCommentedByList[::-1],lengthComments=len(userCommentedByList))
    
