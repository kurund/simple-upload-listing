# Simple file upload and listing application

## Features include
* Ability to upload any files
* Frontend displays the uploaded files
* Only file managers can upload the files

## Setup
1. Clone the project
   > git clone https://github.com/kurund/simple-upload-listing.git
2. Install virtulenv (https://pypi.python.org/pypi/virtualenv)
3. Create and activate virtualenv
   > virtualenv -p python3 env <br/>
   > source env/bin/activate.fish
4. Install required packages
   > pip install -r requirements.txt
5. Setup database
   > cd fileuploadlisting <br/>
   > python manage.py migrate
6. Run the server
   > python manage.py runserver
7. Check if application is running correctly
   > http://127.0.0.1:8000/
8. Create superuser for the admin backend
   > python manage.py createsuperuser
9. Login as superuser
   > http://127.0.0.1:8000/admin
   
###Note
* System already includes following users 
* admin
* file-manager / changeme
   