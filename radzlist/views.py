"""
------------------------------------ Imports ------------------------------------
"""
import requests

from bs4 import BeautifulSoup
from flask import render_template, Blueprint, request, redirect, url_for
from requests.compat import quote_plus

from radzlist import db
from radzlist.forms import SearchForm
from radzlist.models import Search


"""
----------------------------------- Blueprint -----------------------------------
"""
BASE_SEARCH_URL = "https://losangeles.craigslist.org/search/?query={}"
BASE_IMG_URL = "https://images.craigslist.org/{}_300x300.jpg"


"""
----------------------------------- Blueprint -----------------------------------
"""
core = Blueprint('core', __name__)


"""
------------------------------------- Views -------------------------------------
"""
@core.route('/')
def home():
   form = SearchForm()
   return render_template('base.html', form=form)


@core.route('/search', methods=['GET', 'POST'])
def search():
   form = SearchForm()

   if request.method == 'POST':
      new = Search(search=form.search.data)
      db.session.add(new)
      db.session.commit()

      search = form.search.data
      form.search.data = ""
      
      final_url = BASE_SEARCH_URL.format(quote_plus(search))
      response = requests.get(final_url)
      data = response.text
      soup = BeautifulSoup(data, features='html.parser')
      
      posts = soup.find_all('li', class_='result-row')
      final_posts = []

      for post in posts:
         post_title = post.find('a', class_='result-title').text
         post_link = post.find('a', class_='result-title').get('href')

         if post.find('span', class_='result-price'):
            post_price = post.find('span', class_='result-price').text
         else:
            post_price = "N/A"

         if post.find('a', class_='result-image gallery'):
            image_ids = post.find('a', class_='result-image gallery').get('data-ids')
            image_id = image_ids.split(',')[0].split(':')[1]
            post_image = BASE_IMG_URL.format(image_id)
         else:
            post_image = "https://www.craigslist.com/images/peace.jpg"

         final_posts.append((post_title, post_link, post_price, post_image))

      return render_template('search.html', form=form, search=search, final_posts=final_posts)
   else:
      return redirect(url_for('core.home'), form=form)