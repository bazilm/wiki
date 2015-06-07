from google.appengine.ext import db
import sys
import os

sys.path.insert(0,os.path.join(os.path.dirname(__file__),os.pardir,'models'))

from Models import *

def getUsers(username="",password=""):
	if username:
		if password:
			query = db.GqlQuery("SELECT * from Users where username = :1 AND password_hash= :2",username,password)

		else:
			query = db.GqlQuery("SELECT * from Users where username = :1",username)

	else:
		query = db.GqlQuery("SELECT * from Users")

	return query

def getArticles(userid=None,title=""):
	if userid and title:
		pass

	elif userid:
		return Articles.get_by_id(userid)

	elif title:
		pass

	else:
		query = db.GqlQuery("SELECT * from Articles ORDER BY created DESC")

	return query
