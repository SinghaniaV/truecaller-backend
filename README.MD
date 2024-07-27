# Instructions for running the app:

` pip install django`

`python manage.py runserver`

## There are 5 routes in users app:

### /users/login - for logging in the registered user

### /users/logout - for logging out the loggedin user

### /users/add - for adding contacts for a loggedin user

### /users/register - for registering a user 

#### (currenty only supports logging in a user created through Django/admin)

### /users/search_users - for searching the database 

#### (everything works except "But the person’s email is only displayed if the person is a registered user and the user who is searching is in the person’s contact list.")


## There is only one route in identities app (for testing purposes):

### /identities/ - displays all the registered users and the global database
