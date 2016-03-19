# -*- coding: utf-8 -*-
from __future__ import print_function

from flask import jsonify
import random
import string
from werkzeug.exceptions import HTTPException


def generate_id(len=6):
    """
    Generates a new pseudo-random string to serve as shortlink IDs.
    Not collision-proof, but that would be pretty rare.
    """
    id = [random.choice(string.ascii_letters + string.digits) for x in range(len)]
    return ''.join(id)

def error_to_json(exc):
    """
    Converts Flask's default exception output to a simple JSON message.
    """
    response = jsonify(message=str(exc))
    response.status_code = (exc.code if isinstance(exc, HTTPException) else 500)
    return response
