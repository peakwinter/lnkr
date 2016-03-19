# -*- coding: utf-8 -*-
from __future__ import print_function

from flask import Blueprint, jsonify, abort, redirect, request
from flask.views import MethodView

from database import session
from models import Shortlink

viewprint = Blueprint('viewprint', __name__)


class LinkManager(MethodView):
    """
    This MethodView handles creating, obtaining and deleting URL shortlinks.
    """

    def get(self, id):
        # if ID specified, return one
        if id:
            link = Shortlink.query.filter(Shortlink.id == id).first()
            if not link:
                abort(404)
            return jsonify(shortlink=link.json)
        # otherwise return all
        links = Shortlink.query.order_by(Shortlink.created)
        return jsonify(shortlinks=[l.json for l in links]), 200

    def post(self):
        data = request.get_json()
        if not data or not data.get('shortlink') or not data["shortlink"].get('url'):
            abort(400)

        link = Shortlink.query.filter(Shortlink.url == data.get('url')).first()
        if link:
            # if the shortlink already exists, just return the original
            return jsonify(shortlink=link.json), 200
        else:
            # if not, create new shortlink and return it
            link = Shortlink(data.get('url'))
            session.add(link)
            session.commit()
            return jsonify(shortlink=link.json), 201

    def delete(self, id):
        link = Shortlink.query.filter(Shortlink.id == id).first()
        if not link:
            abort(404)
        session.delete(link)
        session.commit()
        return "", 204


class LinkForwarder(MethodView):
    """
    This MethodView uniquely handles the URL redirects when a shortlink is used.
    """

    def get(self, id):
        link = Shortlink.query.filter(Shortlink.id == id).first()
        if not link:
            abort(404)
        # return an HTTP 302 redirect to the proper URL
        response = redirect(link.url, 302)
        response.headers["cache-control"] = "private"
        return response


# register both MethodViews with the Flask URL dispatch
linkmanager_api = LinkManager.as_view('linkmanager_api')
viewprint.add_url_rule('/links', defaults={'id': None},
    view_func=linkmanager_api, methods=['GET',])
viewprint.add_url_rule('/links', view_func=linkmanager_api, methods=['POST',])
viewprint.add_url_rule('/links/<string:id>', view_func=linkmanager_api,
    methods=['GET', 'DELETE'])

linkforwarder_api = LinkForwarder.as_view('linkforwarder_api')
viewprint.add_url_rule('/go/<string:id>', view_func=linkforwarder_api,
    methods=['GET',])
