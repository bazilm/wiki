from Handler import *
import sys
import os

sys.path.insert(0,os.path.join(os.path.dirname(__file__),'utils','lib'))

from validate import *

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
			self.response.headers.add_header('Set-Cookie','userid = %s; Path=/' %str(username))
			self.redirect('/')