from google.appengine.ext import db

class Users(db.Model):
	username = db.StringProperty(required=True)
	passhash = db.StringProperty(required=True)
	email = db.EmailProperty()
	joined = db.DateTimeProperty(auto_now_add = True)



class Articles(db.Model):

	title = db.StringProperty(required = True)
	content = db.TextProperty(required = True)
	created = db.DateTimeProperty(auto_now_add=True)
	userid = db.IntProperty(required = True)
