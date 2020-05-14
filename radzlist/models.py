"""
------------------------------------ Imports ------------------------------------
"""
from radzlist import db
from datetime import datetime


"""
------------------------------------ Models -------------------------------------
"""
class Search(db.Model):

    __tablename__ = "searches"

    id = db.Column(db.Integer, primary_key=True)
    search = db.Column(db.String(500))
    created = db.Column(db.DateTime, nullable=False, default=datetime.now)


    def __init__(self, search):
        self.search = search

    def __repr__(self):
        return self.search

    def as_dict(self):
        return {'search': self.search}