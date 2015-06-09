from google.appengine.ext import db
from google.appengine.api import memcache
import sys
import os

sys.path.insert(0,os.path.join(os.path.dirname(__file__),os.pardir,'models'))

from Models import *

def getUsers(username="",password="" ,userid=None):
	if userid:
		return Users.get_by_id(userid)

	if username:
		if password:
			user = db.GqlQuery("SELECT * from Users where username = :1 AND password_hash= :2",username,password)

		else:
			user = db.GqlQuery("SELECT * from Users where username = :1",username)

	else:
		user = db.GqlQuery("SELECT * from Users")

	return user

def getArticles(articleid=None,title=""):
	if articleid and title:
		pass

	elif articleid:
		articles= Articles.get_by_id(articleid)

	elif title:
		pass

	else:

		articles=memcache.get('articles')
		
		if not articles:
			articles = db.GqlQuery("SELECT * from Articles ORDER BY created DESC")
			memcache.set('articles',list(articles))
	return articles

def putArticle(article):
	articles=memcache.get('articles')
	articles.insert(0,article)
	memcache.set('articles',articles)

def updateCache(articleid,title,content):
	articles=memcache.get('articles')
	for article in articles:
		if article.key().id()==int(articleid):
			article.title=title
			article.content=content
			break
	memcache.set('articles',articles)

