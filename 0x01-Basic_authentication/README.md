# Basic Authentication API

## Overview
Implement Basic Authentication for a simple API. Learn about authentication, Base64 encoding, and securing APIs using Basic Authentication.

## Requirements
- Python 3.7
- Ubuntu 18.04 LTS
- `pip`, `pycodestyle`

## Setup
1. **Clone Repository:**
    ```sh
    git clone https://github.com/yourusername/alx-backend-user-data.git
    cd alx-backend-user-data/0x01-Basic_authentication
    ```
2. **Install Dependencies:**
    ```sh
    pip3 install -r requirements.txt
    ```
3. **Start Server:**
    ```sh
    API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=basic_auth python3 -m api.v1.app
    ```
4. **Test API:**
    ```sh
    curl "http://0.0.0.0:5000/api/v1/status" -vvv
    ```

## Tasks
1. **Simple-basic-API:**
   - Set up and start the server using the provided archive.

2. **Error Handlers:**
   - 401 (Unauthorized): Return `{"error": "Unauthorized"}`.
   - 403 (Forbidden): Return `{"error": "Forbidden"}`.

3. **Auth Class:**
   - Manage API authentication, retrieve authorization headers, and get the current user.

4. **Routes without Authentication:**
   - Update `require_auth` to handle unauthenticated routes.

5. **Request Validation:**
   - Secure API requests using `before_request` in Flask.

6. **BasicAuth Class:**
   - Inherit from `Auth` to handle Basic Authentication.

7. **Base64 Extraction and Decoding:**
   - Extract and decode Base64 strings from the authorization header.

8. **User Credentials:**
   - Extract user email and password from decoded Base64 strings.

9. **User Object:**
   - Return User instance based on email and password.

## Testing
- Use `curl` to test endpoints, both authenticated and unauthenticated requests.

## License
MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing
Pull requests are welcome. Open an issue for major changes.

---

**Note:** For real-world scenarios, use established libraries and frameworks for secure authentication.

