from Handler import *

class SignUpHandler(Handler):

	title = "SignUp"

	def get(self):
		self.render_template('signup.html',title = self.title)

	def post(self):
		username = self.request.get("username")
		password = self.request.get("password")
		email = self.request.get("email")
		self.write(username+" "+password+" "+email)