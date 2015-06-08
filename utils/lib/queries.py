from google.appengine.ext import db
from google.appengine.api import memcache
import sys
import os

sys.path.insert(0,os.path.join(os.path.dirname(__file__),os.pardir,'models'))

from Models import *

def getUsers(username="",password=""):
	if username:
		if password:
			user = db.GqlQuery("SELECT * from Users where username = :1 AND password_hash= :2",username,password)

		else:
			user = db.GqlQuery("SELECT * from Users where username = :1",username)

	else:
		user = db.GqlQuery("SELECT * from Users")

	return user

def getArticles(userid=None,title=""):
	if userid and title:
		pass

	elif userid:
		articles= Articles.get_by_id(userid)

	elif title:
		pass

	else:

		articles=memcache.get('articles')
		
		if not articles:
			articles = db.GqlQuery("SELECT * from Articles ORDER BY created DESC")
			
	return articles

def putArticle(article):
	articles=memcache.get('articles')
	articles.insert(0,article)
	memcache.set('articles',articles)