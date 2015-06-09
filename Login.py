from Handler import *
import sys
import os
import logging

sys.path.insert(0,os.path.join(os.path.dirname(__file__),'utils','lib'))
sys.path.insert(0,os.path.join(os.path.dirname(__file__),'utils','models'))

from validate import *
from queries import *

class LoginHandler(Handler):

	title = "Login"

	def get(self):

		userid = self.request.cookies.get("userid")

		if userid:
			if checkUserId(str(userid)):
				self.redirect('/')
			else:
				self.render_template("login.html",title=self.title)

		else:
			self.render_template("login.html",title=self.title)

	def post(self):
		username = self.request.get("username")
		password = self.request.get("password")
		message = validate(username=username,password=password)
		logging.info(message)
		if message:
			self.render_template("login.html",title = self.title,message=message,
								 username=username)
		else:
			password=getPasswordHash(password)
			userid = self.check_in_users(username,password)
			if not userid :
				self.render_template("login.html",title=self.title,message="Invalid Login")
			
			else:
				userid= setUserId(str(userid))
				self.response.headers.add_header('Set-Cookie','userid = %s; Path=/' %userid)
				self.redirect('/')

	
	def check_in_users(self,username,password):
		users = getUsers(username,password)

		
		if users.count():
			for user in users:
				return user.key().id()
		else:
			return False