from flask import Blueprint,render_template,request,redirect,url_for
from flask_login import login_required,current_user
from .models import Post,Likes
from .import db
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






@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'GET':
        all_posts=Post.query.all()
        userPostInfo=[]
        likesCount=get_likes_count()
        index=0
        for post in all_posts:
       
            user=User.query.filter_by(id=post.userId).first()
            user_id = get_user_id()  
            record = Likes.query.filter_by(postId=post.id, userId=user_id).first()
            record = True if record else False
            userObject={'userFullName':user.firstName+" "+user.lastName,'postedDate':"-".join(str(post.date)[0:10].split('-')[::-1]),'postLikes':likesCount[index],'postId':post.id,'postLiked':record}
            userPostInfo.append(userObject)
            index+=1

    

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

@views.route('/post', methods=['POST','GET'])
@login_required
def post():
    print("In post call")
    if request.method == 'POST':
        data=request.form
        title=data.get('title')
        editorContent=data.get('editor')
        new_post=Post(userId=current_user.id, title=title,content=editorContent)
        db.session.add(new_post)
        db.session.commit()
        #delete_all_posts()

        
        return redirect(url_for('views.home',message="Post Successful", category=True ))
    return render_template('Post.html')