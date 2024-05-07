from flask import Blueprint,render_template,request,redirect,url_for
from flask_login import login_required,current_user
from .models import Post
from .import db
views=Blueprint('views',__name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'GET':
        all_posts=Post.query.all()

        return render_template('Home.html', all_posts=all_posts, postCategory=True)
    else:

        serverMessage=request.args.get('message')
        serverCategory=request.args.get('category')
    
        return render_template('Home.html',message=serverMessage, category=serverCategory)
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

        
        return redirect(url_for('views.home',message="Post Successful", category=True ))
    return render_template('Post.html')