from flask import Blueprint,render_template,request,redirect,url_for
from flask_login import login_required,current_user


views=Blueprint('views',__name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():

    serverMessage=request.args.get('message')
    serverCategory=request.args.get('category')
    
    
    return render_template('Home.html',message=serverMessage, category=serverCategory)