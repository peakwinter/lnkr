# -*- coding: utf-8 -*-
from __future__ import print_function

import datetime
from sqlalchemy import Column, DateTime, Integer, String, text

from .database import Base
from .utils import generate_id


class Shortlink(Base):
    __tablename__ = 'shortlinks'
    id = Column(String, default=generate_id, primary_key=True)
    url = Column(String)
    created = Column(DateTime, default=datetime.datetime.utcnow)

    def __init__(self, url=None, created=None):
        self.url = url
        self.created = created

    def __repr__(self):
        return '<Shortlink {}>'.format(self.id)

    @property
    def json(self):
        return {
            "id": self.id,
            "url": self.url,
            "created": self.created.isoformat()
        }
