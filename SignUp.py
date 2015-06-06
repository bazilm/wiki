from Handler import *
import sys
import os

sys.path.insert(0,os.path.join(os.path.dirname(__file__),'utils','lib'))
sys.path.insert(0,os.path.join(os.path.dirname(__file__),'utils','lib'))

from validate import *
from Models import *
from queries import *

class SignUpHandler(Handler):

	title = "SignUp"

	def get(self):
		self.render_template('signup.html',title = self.title)

	def post(self):
		username = self.request.get("username")
		password = self.request.get("password")
		verify = self.request.get("verify")
		email = self.request.get("email")

		message = validate(username=username,password=password,
							verify = verify,email=email)

		if message:
			self.render_template('signup.html',title=self.title,
								  username=username,message=message)

		else:
			if self.check_in_users(username):
				self.render_template('signup.html',title=self.title,
									 message="Username Taken")

			else:
				user = Users(username=username,password_hash=password,email=email)
				user.put()
				self.response.headers.add_header('Set-Cookie','userid = %s; Path=/' %str(username))
				self.redirect('/')


	def check_in_users(self,username):
		users = getUsers(username)

		if users:
			return False
		else:
			return True