from flask import Blueprint, abort, jsonify, redirect, request
import os
import requests
from http import HTTPStatus
from werkzeug.exceptions import HTTPException


def get_check_token(token):
    response = requests.get(os.environ.get("CHECK_TOKEN"), headers={ 'Authorization': 'Bearer '+ token })
    print(response.text)
    if response.ok:
        return True

    return False






