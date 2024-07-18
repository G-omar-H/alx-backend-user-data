#!/usr/bin/env python3
"""
app.py
"""
from flask import Flask, jsonify, request, abort, make_response
from auth import Auth

app = Flask(__name__)

AUTH = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def welcom():
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users() -> str:
    """
    end-point to register a user
    """
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        AUTH.register_user(email=email, password=password)
        return jsonify({"email": f"{email}", "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    """
    login the user
    """
    email = request.form.get('email')
    password = request.form.get('password')
    if not AUTH.valid_login(email, password):
        abort(401)
    response = make_response(
        jsonify({"email": f"{email}", "message": "logged in"}))
    response.set_cookie('session_id', AUTH.create_session(email))
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
