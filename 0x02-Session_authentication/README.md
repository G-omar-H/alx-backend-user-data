# 0x02. Session Authentication Back-end Authentication

## Project Overview

**Duration:** July 10, 2024, 4:00 AM to July 12, 2024, 4:00 AM

**Auto QA Review:**
- Mandatory: 0.0/135
- Optional: 0.0/46
- Altogether: 0.0%
  - Mandatory: 0.0%
  - Optional: 0.0%

## In a Nutshell

In this project, we implement a Session Authentication system without using any external modules. While in the industry, we typically use existing modules or frameworks like Flask-HTTPAuth, here we build each step from scratch to gain a deep understanding of the mechanism.

## Background Context

- **Session Authentication:** Implement a session-based authentication system.
- **Cookies:** Understanding and utilizing HTTP cookies.

## Resources

- **Read or Watch:**
  - REST API Authentication Mechanisms (session auth part)
  - HTTP Cookie
  - Flask
  - Flask Cookie

## Learning Objectives

By the end of this project, you will be able to explain the following without Google:

1. What authentication means
2. What session authentication means
3. What Cookies are
4. How to send Cookies
5. How to parse Cookies

## Requirements

### Python Scripts

- Compatible with Ubuntu 18.04 LTS using python3 (version 3.7)
- Files should end with a new line
- First line of all files: `#!/usr/bin/env python3`
- Follow pycodestyle (version 2.5)
- Files must be executable
- Documentation required for all modules, classes, and functions

### Documentation

- Each module, class, and method must have a descriptive docstring explaining its purpose.

## Tasks

### 0. Et moi et moi et moi!

- Copy all work from the 0x06. Basic authentication project.
- Add a new endpoint: `GET /users/me` to retrieve the authenticated User object.
- Update `@app.before_request` in `api/v1/app.py` to assign the result of `auth.current_user(request)` to `request.current_user`.
- Update method for `GET /api/v1/users/<user_id>` in `api/v1/views/users.py`.

### 1. Empty session

- Create a class `SessionAuth` that inherits from `Auth`.
- Update `api/v1/app.py` to use `SessionAuth` based on the environment variable `AUTH_TYPE`.

### 2. Create a session

- Update `SessionAuth` class:
  - Create `user_id_by_session_id` dictionary.
  - Implement `create_session(self, user_id: str = None) -> str`.

### 3. User ID for Session ID

- Implement `user_id_for_session_id(self, session_id: str = None) -> str` in `SessionAuth`.

### 4. Session cookie

- Add `session_cookie(self, request=None)` method to `api/v1/auth/auth.py`.

### 5. Before request

- Update `@app.before_request` method in `api/v1/app.py`:
  - Exclude `/api/v1/auth_session/login/` from `require_auth`.
  - Abort with 401 if both `auth.authorization_header(request)` and `auth.session_cookie(request)` return None.

### 6. Use Session ID for identifying a User

- Implement `current_user(self, request=None)` in `SessionAuth`.

## Usage

To run the project:

```bash
# Set environment variables
export API_HOST=0.0.0.0
export API_PORT=5000
export AUTH_TYPE=session_auth
export SESSION_NAME=_my_session_id

# Start the application
python3 -m api.v1.app
```

## Testing

To test the application, you can use curl commands:

```bash

# Check status
curl "http://0.0.0.0:5000/api/v1/status"

# Attempt unauthorized access
curl "http://0.0.0.0:5000/api/v1/users/me"

# Access with session ID
curl "http://0.0.0.0:5000/api/v1/users/me" --cookie "_my_session_id=<your_session_id>"
```

## Repository

    GitHub repository: alx-backend-user-data
    Directory: 0x02-Session_authentication
    Files:
        api/v1/app.py
        api/v1/views/users.py
        api/v1/auth/session_auth.py
        api/v1/auth/auth.py
