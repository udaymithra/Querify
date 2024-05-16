import re
from flask import Blueprint, render_template,  request, redirect, url_for
from .models import User
from . import db   
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required,logout_user,current_user
def is_valid_email(email):
 

  # Common email address regex pattern
  pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$)"

  # Check if the email matches the pattern
  if re.match(pattern, email):
    return True
  else:
    return False
  
def is_valid_password(password):
  """
  This function checks if a given string is a valid password using regular expressions.

  Args:
      password: The password string to validate.

  Returns:
      True if the password is valid, False otherwise.
  """

  # Password complexity requirements (adjust as needed)
  # - At least 8 characters long
  # - Contains at least one uppercase letter, lowercase letter, number, and special character
  pattern = r"(^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])(?=.{8,}$))"

  # Check if the password matches the pattern
  if re.match(pattern, password):
    return True
  else:
    return False


auth=Blueprint('auth',__name__)





def is_valid_password(password):
 
  # Password complexity requirements (adjust as needed)
  # - At least 8 characters long
  # - Contains at least one uppercase letter, lowercase letter, number, and special character
  pattern = r"(^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])(?=.{8,}$))"

  # Check if the password matches the pattern
  if re.match(pattern, password):
    return True
  else:
    return False


@auth.route('/login', methods=['GET', 'POST'])

def login():
    if request.method == 'POST':

        data = request.form
        print(data)

        emailAddress=data.get('email')
        password=data.get('password')
        user=User.query.filter_by(emailAddress=emailAddress).first()
        if user:
            if check_password_hash(user.password,password):
               login_user(user,remember=True)
               print(current_user)
               return redirect(url_for('views.home',message="Login Successful", category=True))
            else:
               return render_template('login.html', message='Invalid Password, try again', category=False)
        else:
           print("user not found")
           return render_template('login.html', message='User not found', category=False)
    else:
       if current_user.is_authenticated:
          return redirect(url_for('views.home',message="Login Successful", category=True,current_user=current_user))
       else:
          return render_template('Login.html')


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
@auth.route('/signup',methods=['GET', 'POST'])

def signup():
    print("signup called")
    if request.method == 'POST':
       data= request.form
       firstName=data.get('firstName')
       lastName=data.get('lastName')
       emailAddress=data.get('email')
       password1=data.get('password1')
       password2=data.get('password2')


       if(len(firstName)<2) :
          return render_template('Signup.html', message="First name must be at least 2 characters" , category=False)
       elif(is_valid_email(emailAddress)==False):
          return render_template('Signup.html', message="Invalid Email Address", category=False)
       elif (password1!=password2):
          return render_template('Signup.html', message="Confirm Password doesn't match", category=False)
       elif(is_valid_password(password1)==False):
            return render_template('Signup.html', message="Password requires at least 8 characters long and contains at least one uppercase letter, lowercase letter, number, and special character ", category=False)
       
       else:
          
          user=User.query.filter_by(emailAddress=emailAddress).first()
          if user:
             return render_template('Signup.html', message="Email Address already in use", category=False)
          else:
            new_user= User(emailAddress=emailAddress, firstName=firstName, lastName=lastName, password=generate_password_hash(password1, method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user,remember=True)
            return redirect(url_for('views.home',message="Account created successfully!", category=True,current_user=current_user))
          #return render_template('Signup.html', message="Account created successfully!", category=True )
       
    return render_template('Signup.html', text="testing")