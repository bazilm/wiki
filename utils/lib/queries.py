from google.appengine.ext import db

def getUsers(username="",password=""):
	if username:
		if password:
			query = db.GqlQuery("SELECT * from Users where username = :1 AND password_hash= :2",username,password)

		else:
			query = db.GqlQuery("SELECT * from Users where username = :1",username)

	else:
		query = db.GqlQuery("SELECT * from Users")

	return query