# -*- coding: utf-8 -*-
from __future__ import print_function

from flask import Flask
from werkzeug.exceptions import default_exceptions

from views import viewprint
from database import init_db, session
from utils import error_to_json

# Set runlevel here
DEBUG = True


def create_app(env='Defaults'):
    """
    Creates application and connects to database file.
    """
    app = Flask(__name__)
    app.config["DEBUG"] = DEBUG
    app.register_blueprint(viewprint)
    for code in default_exceptions.iterkeys():
        app.error_handler_spec[None][code] = error_to_json
    init_db()
    return app

def shutdown_session(exception=None):
    """
    Removes the database connection on app quit/teardown.
    """
    session.remove()


app = create_app()
app.teardown_appcontext(shutdown_session)
