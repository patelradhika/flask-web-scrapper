"""
------------------------------------ Imports ------------------------------------
"""
from datetime import datetime
from webscrapper import db


"""
------------------------------------ Models -------------------------------------
"""
class Search(db.Models):

    __tablename__ = "search"

    search = db.Column(db.String(500))
    created = db.Column(db.DateTime(default=datetime.now)

    def __repr__(self):
        return self.search