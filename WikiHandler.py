from Handler import *

class WikiHandler(Handler):

	template='wiki.html'
	title = 'Welcome to Wiki'
	status = "login"
	add = ""


	def get(self):

		userid = self.request.cookies.get('userid')

		if userid:
			self.add = 'Add'
			self.status='logout'
			self.render(self.template,title=self.title,
						add=self.add,status=self.status)
		else:
			self.render(self.template,title=self.title,
						add=self.add,status=self.status)