from Handler import *

class WikiHandler(Handler):

	template='wiki.html'
	title = 'Welcome to Wiki'
	status = "logout"
	add = "add"


	def get(self):
		self.render(self.template,title=self.title,
					add=self.add,status=self.status)