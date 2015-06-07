from Handler import *
import sys
import os

sys.path.insert(0,os.path.join(os.path.dirname(__file__),'utils','lib'))
sys.path.insert(0,os.path.join(os.path.dirname(__file__),'utils','models'))

from validate import *
from queries import *
from Models import *


class AddEditHandler(Handler):

	title = ""

	def get(self):

		status = self.request.get("q")
		self.title=self.set_title(status)
		if self.title:
			self.render("addedit.html",title=self.title)


	def post(self):
		status = self.request.get('q')
		self.title=self.set_title(status)

		if self.title:
			post_title = self.request.get('title')
			post_content= self.request.get('content')
			message = validate_post(post_title,post_content)
			userid = self.request.cookies.get("userid")
		
			if message==True:
				userid = self.request.cookies.get("userid")

				if checkUserId(str(userid)):
					post_content=post_content.replace('\n','<br>')
					userid = int(userid.split('|')[0])
					article = Articles(title=post_title,content=post_content,
										user_id=userid)
					article.put()
					self.redirect('/')

				else:
					self.redirect('/login')
				
			else:
				self.render('addedit.html',title=self.title,post_title=post_title,
							post_content=post_content,message=message)


	def set_title(self,status):
		if status=="add":
			return "Add"
		elif status =="edit":
			return "Edit"
		else:
			return None

