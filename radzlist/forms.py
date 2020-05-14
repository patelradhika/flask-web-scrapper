"""
------------------------------------ Imports ------------------------------------
"""
from flask_wtf import FlaskForm
from wtforms import StringField


"""
------------------------------------- Forms -------------------------------------
"""
class SearchForm(FlaskForm):
    search = StringField("Search")