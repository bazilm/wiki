import re
import hashlib
SECRET = "qwenmwerczcv1267"

username_regex = '([a-zA-Z0-9-_]{3,16}$)'
password_regex = '([a-zA-Z0-9-_]{6,20}$)'
email_regex = '(.{1,16})@(.{3,10}).com'
message = False

def validate(username,password,verify=None,email=None):
	username_match=re.match(username_regex,str(username))
	global message
	
	if username_match:
		password_match = re.match(password_regex,str(password))

		if password_match:
			if verify:
				if password==verify:
					if email:
						email_match = re.match(email_regex,str(email))

						if  email_match:
							pass
						else:
							message = "Invalid email"

				else:
					message="Passwords doesn't match"
		else:
			message = "Invalid Password"

	else:
		message = "Invalid Username"

	return message

def validate_post(title,content):

	if title and content:
		return True
	else:
		if title:
			return "Content required"

		elif content:
			return "Title required"

		else:
			return "Title and Content required"

def setUserId(username):
	userid = username+'|'+hashlib.sha256(SECRET+username).hexdigest()
	return userid

def checkUserId(userid):
	userid = userid.split('|')

	if len(userid)<=1:
		return False

	username=userid[0]
	username_hash=userid[1]


	if hashlib.sha256(SECRET+username).hexdigest()==username_hash:
		return True
	else:
		return False

def getPasswordHash(password):
	return hashlib.sha256(SECRET+password).hexdigest()


def updateCache(articleid,title,content):
	articles=memcache.get('articles')
	for article in articles:
		if article.key().id()==int(articleid):
			article.title=title
			article.content=content


