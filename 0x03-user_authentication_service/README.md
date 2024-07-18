# User Authentication Service - 0x03

## Overview

This project aims to build a complete user authentication service using Python and Flask. The project walks through the steps to understand and implement user authentication mechanisms. For learning purposes, we are not using pre-built modules like Flask-User, but implementing the mechanisms from scratch.

## Table of Contents
- [Resources](#resources)
- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
- [Setup](#setup)
- [Tasks](#tasks)
  - [0. User Model](#0-user-model)
  - [1. Create User](#1-create-user)
  - [2. Find User](#2-find-user)
  - [3. Update User](#3-update-user)
  - [4. Hash Password](#4-hash-password)
  - [5. Register User](#5-register-user)
  - [6. Basic Flask App](#6-basic-flask-app)
  - [7. Register User Endpoint](#7-register-user-endpoint)
  - [8. Credentials Validation](#8-credentials-validation)
  - [9. Generate UUIDs](#9-generate-uuids)
  - [10. Get Session ID](#10-get-session-id)
  - [11. Log In](#11-log-in)
  - [12. Find User by Session ID](#12-find-user-by-session-id)
  - [13. Destroy Session](#13-destroy-session)
  - [14. Log Out](#14-log-out)
  - [15. User Profile](#15-user-profile)

## Resources

Read or watch:
- [Flask documentation](https://flask.palletsprojects.com/en/2.0.x/)
- [Requests module](https://docs.python-requests.org/en/latest/)
- [HTTP status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

## Learning Objectives

By the end of this project, you will be able to:
- Declare API routes in a Flask app
- Get and set cookies
- Retrieve request form data
- Return various HTTP status codes

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 18.04 LTS using `python3` (version 3.7)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/env python3`
- A `README.md` file, at the root of the project folder, is mandatory
- Your code should use the `pycodestyle` style (version 2.5)
- You should use SQLAlchemy 1.3.x
- All files must be executable
- The length of your files will be tested using `wc`
- All modules should have a documentation string (docstring)
- All classes should have a documentation string (docstring)
- All functions (inside and outside a class) should have a documentation string (docstring)
- All functions should be type annotated
- The Flask app should only interact with Auth and never with the DB directly
- Only public methods of Auth and DB should be used outside these classes

## Setup

You will need to install `bcrypt`:

```bash
pip3 install bcrypt
```

## Tasks

0. User Model

Create a SQLAlchemy model named User for a database table named users.

Attributes:

    id: integer primary key
    email: non-nullable string
    hashed_password: non-nullable string
    session_id: nullable string
    reset_token: nullable string

1. Create User

Complete the DB class to implement the add_user method. This method should save a user to the database with the given email and hashed_password.

2. Find User

Implement the DB.find_user_by method. This method should return the first row found in the users table as filtered by the method’s input arguments. Raise NoResultFound and InvalidRequestError appropriately.

3. Update User

Implement the DB.update_user method that updates a user's attributes and commits the changes to the database. Raise a ValueError for invalid arguments.

4. Hash Password

Define a _hash_password method that returns a salted hash of the input password using bcrypt.

5. Register User

Implement the Auth.register_user method. If a user already exists with the provided email, raise a ValueError. Otherwise, hash the password, save the user to the database, and return the User object.

6. Basic Flask App

Set up a basic Flask app with a single GET route ("/") that returns a JSON payload: {"message": "Bienvenue"}.

7. Register User Endpoint

Implement the POST /users route to register a user. Return appropriate JSON payloads for successful registration and already registered emails.

8. Credentials Validation

Implement the Auth.valid_login method to validate email and password.

9. Generate UUIDs

Implement a _generate_uuid function that returns a string representation of a new UUID.

10. Get Session ID

Implement the Auth.create_session method to generate and store a session ID for a user, and return the session ID.

11. Log In

Implement the POST /sessions route to log in a user and set the session ID as a cookie.

12. Find User by Session ID

Implement the Auth.get_user_from_session_id method to find and return the user corresponding to the session ID.

13. Destroy Session

Implement Auth.destroy_session to update the user's session ID to None.

14. Log Out

Implement the DELETE /sessions route to log out a user by destroying their session and redirecting to GET /.

15. User Profile

Implement the GET /profile route to return the user's email if a valid session ID is provided. Return a 403 status code for invalid session IDs or non-existent users.

## Repository

    GitHub repository: alx-backend-user-data
    Directory: 0x03-user_authentication_service

## License

This project is licensed under the MIT License - see the LICENSE file for details.
