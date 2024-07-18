#!/usr/bin/env python3
"""
Main file
"""
import requests


def check_response_is_json(response):
    """ Check if the response content type is JSON """
    if response.headers.get('Content-Type') == 'application/json':
        return response.json()
    return None


def register_user(email: str, password: str) -> None:
    """ Register a new user """
    response = requests.post(
        'http://127.0.0.1:5000/users',
        data={
            'email': email,
            'password': password})
    assert response.status_code == 200
    assert response.json() == {"email": email, "message": "user created"}


def log_in_wrong_password(email: str, password: str) -> None:
    """ Attempt to log in with wrong password """
    response = requests.post(
        'http://127.0.0.1:5000/sessions',
        data={
            'email': email,
            'password': password})
    assert response.status_code == 401
    json_response = check_response_is_json(response)
    if json_response:
        assert json_response == {"message": "invalid credentials"}
    else:
        assert "Unauthorized" in response.text


def log_in(email: str, password: str) -> str:
    """ Log in with correct credentials """
    response = requests.post(
        'http://127.0.0.1:5000/sessions',
        data={
            'email': email,
            'password': password})
    assert response.status_code == 200
    assert response.json() == {"email": email, "message": "logged in"}
    return response.cookies.get('session_id')


def profile_unlogged() -> None:
    """ Attempt to access profile without being logged in """
    response = requests.get('http://127.0.0.1:5000/profile')
    assert response.status_code == 403
    json_response = check_response_is_json(response)
    if json_response:
        assert json_response == {"message": "forbidden"}
    else:
        assert "Forbidden" in response.text


def profile_logged(session_id: str) -> None:
    """ Access profile while logged in """
    response = requests.get(
        'http://127.0.0.1:5000/profile',
        cookies={
            'session_id': session_id})
    assert response.status_code == 200
    assert "email" in response.json()


def log_out(session_id: str) -> None:
    """ Log out from the session """
    response = requests.delete(
        'http://127.0.0.1:5000/sessions',
        cookies={
            'session_id': session_id})
    assert response.status_code == 200
    assert response.url == 'http://127.0.0.1:5000/'


def reset_password_token(email: str) -> str:
    """ Request a password reset token """
    response = requests.post(
        'http://127.0.0.1:5000/reset_password',
        data={
            'email': email})
    assert response.status_code == 200
    return response.json().get('reset_token')


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """ Update the password using the reset token """
    response = requests.put('http://127.0.0.1:5000/reset_password', data={
        'email': email,
        'reset_token': reset_token,
        'new_password': new_password
    })
    assert response.status_code == 200
    assert response.json() == {"email": email, "message": "Password updated"}


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"

if __name__ == "__main__":
    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
