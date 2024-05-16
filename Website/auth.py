import re
from flask import Blueprint, render_template,  request, redirect, url_for
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
    return render_template('Login.html')


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
@auth.route('/signup',methods=['GET', 'POST'])

def signup():
    return render_template('Signup.html')