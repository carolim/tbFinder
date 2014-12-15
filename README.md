CIS 192 Final Project: TbFinder

DOCUMENTATION
We created a Flask webapp specifically for Penn students, that allows them to find and post online links to textbooks they have found, for classes they've taken. 

The app is callable from the command line, using the command 'python runserver.py' when in the top-level directory. Additionally, the following two flags can be used to determine its usage (see also 'python runserver.py -h'):
'-d / --debug': runs the app in debug mode
'-p / --setport': controls which port the local server runs on.

Upon verification that the email entered is a Penn email, the user should be able to log in and browse links to all textbooks currently available, that have been previously uploaded by other users. If the user wishes to post a link to a textbook, there is a form that he/she can fill up. After submitting it, the information will be stored in the existing database and displayed on the main page. Users can also view pages for specific classes within a particular department (eg. 'CIS 110') that contain only links to that specific class. 

