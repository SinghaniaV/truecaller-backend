# CallerID App

This project is a REST API designed to be consumed by a mobile app, similar to popular apps that identify spam numbers or allow searching for a person's name by their phone number. 

## Overview

The API provides functionalities for user registration, contact management, spam identification, and search capabilities for identifying users by their phone number or name.

## Database Requirements

- Relational database with an ORM (Object-Relational Mapping) for persistence.

## Terminology and Assumptions

- **Registered User**: A user who has signed up on the app.
- **Contacts**: Each registered user can have zero or more personal contacts.
- **Global Database**: Combination of all registered users and their personal contacts.

## Data Storage Requirements

### User Information

- **Name**
- **Phone Number**
- **Email Address** (optional)

## Features

### Registration and Profile

- Users must register with a name, phone number, and password.
- Only one user can register with a particular phone number.
- Users must be logged in to access any functionality.
- User’s phone contacts are automatically imported into the app’s database.

### Spam Identification

- Users can mark a number as spam, which will be reflected in the global database.
- The spam number may or may not belong to a registered user or contact.

### Search Functionality

#### By Name:

- Search for a person by name in the global database.
- Results display name, phone number, and spam likelihood.
- Results prioritize names starting with the search query, followed by names containing the query.

#### By Phone Number:

- Search for a person by phone number in the global database.
- If a registered user has the phone number, show only that result.
- Otherwise, show all matches for that phone number.

### Detail View:

- Clicking a search result displays all details for that person.
- Email is displayed only if the person is a registered user and the searcher is in their contact list.

### Data Population

- A script to populate the database with a significant amount of random, sample data for testing.

## Installation and Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/SinghaniaV/truecaller-backend
    cd truecaller-backend
    ```

2. **Install dependencies**:
    ```bash
    pip install django
    ```

3. **Run the server**:
    ```bash
    python manage.py runserver
    ```

## API Endpoints

### Users App

- **/users/login**: For logging in the registered user.
- **/users/logout**: For logging out the logged-in user.
- **/users/add_users**: For adding contacts for a logged-in user.
- **/users/register**: For registering a user.
- **/users/search_users**: For searching the database.

### Identities App

- **/identities/**: Displays all the registered users and the global database with their saved contacts (for testing purposes).
