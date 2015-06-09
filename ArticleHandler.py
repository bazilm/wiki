from Handler import *
import sys
import os
import logging

sys.path.insert(0,os.path.join(os.path.dirname(__file__),'utils','lib'))

from validate import *
from queries import *

class ArticleHandler(Handler):

	title = ''
	def get(self,article_id):

		userid = self.request.cookies.get('userid')
		if checkUserId(str(userid)):
			self.title='Edit'
		
		
		article = getArticles(int(article_id))
		self.render('article.html',post_title=article.title,title=self.title,
					post_content=article.content,post_id=article.key().id(),
					post_username=article.username,post_created=str(article.created.date()),
					post_modified=str(article.last_modified.date()))

