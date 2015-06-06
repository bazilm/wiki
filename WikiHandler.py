from Handler import *

class WikiHandler(Handler):

	template='wiki.html'
	title = 'Welcome to Wiki'


	def get(self):
		self.render(self.template,title=self.title)