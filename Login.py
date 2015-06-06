from Handler import *

class LoginHandler(Handler):

	title = "Login"

	def get(self):
		self.render_template("login.html",title=self.title)

	def post(self):
		username = self.request.get("username")
		password = self.request.get("password")
		self.write(username+"\n"+password)

	def render_template(self,template,title="",username="",message=""):
		self.render(template,title=title,username=username,
					message=message)