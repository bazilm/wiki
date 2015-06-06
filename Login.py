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
			self.redirect('/')
		else:
			self.render_template("login.html",title=self.title)

	def post(self):
		username = self.request.get("username")
		password = self.request.get("password")
		message = validate(username=username,password=password)
		
		if message:
			self.render_template("login.html",title = self.title,message=message,
								 username=username)
		else:
			if not self.check_in_users(username,password):
				self.render_template("login.html",title=self.title,message="Username not registered")
			
			else:
				self.response.headers.add_header('Set-Cookie','userid = %s; Path=/' %str(username))
				self.redirect('/')

	
	def check_in_users(self,username,password):
		users = getUsers(username,password)

		logging.info('logging')

		for user in users:
			logging.info(user.username+" "+user.password_hash)
		
		if users.count():
			return True
		else:
			return False