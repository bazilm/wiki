from Handler import *
import sys
import os

from google.appengine.api import memcache
sys.path.insert(0,os.path.join(os.path.dirname(__file__),'utils','lib'))
sys.path.insert(0,os.path.join(os.path.dirname(__file__),'utils','models'))

from validate import *
from queries import *
from Models import *


class AddEditHandler(Handler):

	title = "Add Page"

	def get(self):
		userid = self.request.cookies.get('userid')
		if checkUserId(str(userid)):
			self.render('addedit.html',title=self.title)
		else:
			self.redirect('/')


	def post(self):
		post_title = self.request.get('title')
		post_content= self.request.get('content')
		message = validate_post(post_title,post_content)
			
		
		if message==True:
			userid = self.request.cookies.get("userid")

			if checkUserId(str(userid)):
					post_content=post_content.replace('\n','<br>')
					userid = int(userid.split('|')[0])
					username=getUsers(userid=userid).username
					article = Articles(title=post_title,content=post_content,
										user_id=userid,username=username)
					article.put()
					putArticle(article)
					self.redirect('/')

			else:
					self.redirect('/login')
				
		else:
			self.render('addedit.html',title=self.title,post_title=post_title,
							post_content=post_content,message=message)


