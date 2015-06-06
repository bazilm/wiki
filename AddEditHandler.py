from Handler import *

class AddEditHandler(Handler):

	title = "Add"

	def get(self):
		self.render("addedit.html",title=self.title)

