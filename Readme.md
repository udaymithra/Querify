Querify

A Feature-Rich Querying Platform

Project Description

Querify is a comprehensive online platform designed to facilitate effective querying, discussion, and collaboration. Users can create and edit posts, format text, react to posts and comments, and engage in interactive threaded discussions. Built with responsiveness in mind, Querify offers an exceptional user experience across various devices.

Key Features

Robust Authentication: Secure login and signup processes ensure user privacy and identity management.
Interactive Pop-Up Notifications: Real-time visual feedback for validation and error messages.
Rich Text Formatting: Enhance posts with bold, italics, links, and image embedding capabilities.
Pre-Submission Editing: Refine your queries before finalizing them.
Real-Time Reactions: Add a layer of interaction with post-like and dislike features.
Comprehensive Commenting: Engage in threaded discussions with nested replies.
Comment Reactions: Express your opinion on comments using likes and dislikes.
Selective Comment Deletion: Users can delete their own comments to maintain control over their contributions.
Contextual Comment Toolbar: Highlight text to seamlessly access the comment/reply toolbar.
Read More/Less Functionality: Manage post and comment length for improved readability.
View All Comments: Access complete comment threads without limitations.
Powerful Search: Find relevant information quickly and efficiently.
User Profile Management: Edit your profile details to personalize your experience.
Post Deletion: Remove unnecessary or outdated posts for a clean and organized environment.
Responsive Mobile UI: Enjoy a seamless user experience on smartphones and other mobile devices.
Integrated Bottom Navigation for easy navigation.
Optimized Search Bar for convenient information retrieval.
Logout and Session Management: Securely log out and maintain session control.
Password Toggling: Switch between showing and hiding your password for added security.


2.Group-member details

UWA ID	        Name	                    Github User Name
23872782	Shanmugapriya Sankarraj	        Sem3group
23858856	Udaymithra Kalla	            udaymithra
23870369	Dharani Kumari Nagali	        dharaninagala
23832048	Gnaneshwar Reddy Bana	        gnaneshwarbana



3.Instructions to launch the application:

1.Clone or Download the Project Source code:
Download the code from github by cloning it or from zip folder 
2.Install python using the following command:
For MacOS:
Follow the instructions given in the following website:
https://www.python.org/downloads/macos/

For Windows:
Follow the instructions given in the following website:
https://www.python.org/downloads/windows/

For Linux/UNIX:
Follow the instructions given in the following website:
https://www.python.org/downloads/source/

3.Install pip3 using the following command in terminal:
sudo apt install python3-pip

4.Install dependencies:
Install these required libraries in the terminal using the following commands:
pip3 install flask
pip3 install flask-login
pip3 install flask-sqlalchemy
pip3 install Flask-SocketIO
pip3 install flask_humanize

5.Run the Application:
Once after done with downloading and installing we now run the application using the following command:
python3 main.py 

6.Access the app
We get a local URL to access the website. Copy and paste the URL in a web browser and go through our user-friendly website. 


4.Instructions for Running Tests for the Application

1.Setup Environment:Install all the required libraries in terminal.This can be done by using pip 
pip3 install -r requirements.txt

requirements.txt contains:
selenium
webdriver-manager
pytest
pytest-cov
pytest-html

or individually you can install  for example: pip3 install selenium

2.Running Unit Tests:
Unit tests are located in the tests/unit directory. To run all the unit tests:
python3 -m pytest tests/unit 

3.Running Selenium WebDriver Tests:
Selenium WebDriver tests are located in the tests/selenium_webdrive_tests directory. To run all the Selenium tests and  use the following command:
python3 -m pytest tests/selenium_webdriver_tests/

4.To run the tests individually for example(test_login.py)
python3 -m pytest tests/selenium_webdriver_tests/test_login.py

To run a specific unit test file for example(test_createpostunit.py)

python3 -m pytest tests/unit/test_createpostunit.py





