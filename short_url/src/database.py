from sqlalchemy.dialects.postgresql import UUID
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

import string
import random

db = SQLAlchemy()


class UrlShortener(db.Model):
    
    __tablename__ = "url_shortner" 

    id=db.Column(db.Integer, primary_key=True)
    url_title=db.Column(db.Text, nullable=True)
    url=db.Column(db.Text, nullable=False)
    short_url=db.Column(db.String, nullable=True)
    visits_count = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, onupdate=datetime.now())
    visitors = db.relationship("UrlVisitors", backref="urls")

    def generate_short_characters(self):
        characters = string.digits + string.ascii_letters
        pciked_chars = ''.join(random.choices(characters,k=4))

        link = self.query.filter_by(short_url = pciked_chars).first()

        if link:
            self.generate_short_characters()
        else:
            return pciked_chars

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.short_url = self.generate_short_characters()

    # def __repr__(self) -> str:
    #     return f'Link >>> {self.id}'

class UrlVisitors(db.Model):
    __tablename__ = "url_visitors" 

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(UUID(), nullable = True)
    url_id = db.Column(db.Integer, db.ForeignKey("url_shortner.id"))
    where = db.Column(db.String, nullable=False)
    browser_info = db.Column(db.String(120), unique=False, nullable=False)
    device_ip = db.Column(db.String(120), nullable=False)
    device_visits_count = db.Column(db.Integer, default=1)
    device_visit_date = db.Column(db.DateTime, default=datetime.now())
