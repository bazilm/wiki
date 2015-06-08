from Handler import *
import sys
import os

sys.path.insert(0,os.path.join(os.path.dirname(__file__),'utils','models'))
sys.path.insert(0,os.path.join(os.path.dirname(__file__),'utils','lib'))


from validate import *
from queries import *
from Models import *

class EditHandler(Handler):

	title = "Edit"

	def get(self,article_id):

		userid = self.request.cookies.get('userid')
		if checkUserId(str(userid)):
			article = getArticles(int(article_id))

			self.render('addedit.html',title=self.title,post_title=article.title,
						post_content=article.content)
		else:
			self.redirect('/')


	def post(self,article_id):

		post_title = self.request.get('title')
		post_content = self.request.get('content')

		message = validate_post(post_title,post_content)

		if message==True:
			article = getArticles(int(article_id))

			article.title=post_title
			article.content=post_content
			article.put()
			updateCache(article_id,post_title,post_content)
			self.redirect('/')

		else:
			self.render('addedit.html',title=self.title,post_title=post_title,
						post_content=post_content,message=message)


