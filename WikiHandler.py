from Handler import *
import sys
import os

sys.path.insert(0,os.path.join(os.path.dirname(__file__),'utils','lib'))

from validate import *
from queries import *

class WikiHandler(Handler):

	template='wiki.html'
	title = 'Welcome to Wiki'
	status = "login"
	add = ""


	def get(self):

		userid = self.request.cookies.get('userid')
		articles = list(getArticles())

		if checkUserId(str(userid)):
			self.add = 'Add'
			self.status='logout'
			self.render(self.template,title=self.title,
						add=self.add,status=self.status,articles=articles)
		else:
			self.render(self.template,title=self.title,
						add=self.add,status=self.status,articles=articles)