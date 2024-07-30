## Overview

Created a REST API to be consumed by a mobile app, similar to popular apps that identify spam numbers or allow searching for a person's name by their phone number.

**Database Requirements:**
- Use a relational database with an ORM for persistence.
  
## Terminology and Assumptions

- **Registered User**: A user who has signed up on the app.
- **Contacts**: Each registered user can have zero or more personal contacts.
- **Global Database**: Combination of all registered users and their personal contacts.

## Data Storage Requirements

- **User Information**: 
  - Name
  - Phone Number
  - Email Address (optional)

## Registration and Profile

- Users must register with a name, phone number, and password.
- Only one user can register with a particular phone number.
- Users must be logged in to access any functionality.
- User’s phone contacts are automatically imported into the app’s database.

## Spam Identification

- Users can mark a number as spam, which will be reflected in the global database.
- The spam number may or may not belong to a registered user or contact.

## Search Functionality

- **By Name**:
  - Search for a person by name in the global database.
  - Results display name, phone number, and spam likelihood.
  - Results prioritize names starting with the search query, followed by names containing the query.

- **By Phone Number**:
  - Search for a person by phone number in the global database.
  - If a registered user has the phone number, show only that result.
  - Otherwise, show all matches for that phone number.

**Detail View**:
- Clicking a search result displays all details for that person.
- Email is displayed only if the person is a registered user and the searcher is in their contact list.

## Data Population

- A script to populate the database with a significant amount of random, sample data for testing.

---

# Instructions for running the App:
`cd callerID`

`pip install django`

`python manage.py runserver`

## There are 5 routes in users app:

- `/users/login` - for logging in the registered user

- `/users/logout` - for logging out the loggedin user

- `/users/add_users` - for adding contacts for a loggedin user

- `/users/register` - for registering a user

- `/users/search_users` - for searching the database

## There is only one route in identities app (for testing purposes):

- `/identities/` - displays all the registered users and the global database with their saved contacts
