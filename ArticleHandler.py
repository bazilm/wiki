from Handler import *
import sys
import os
import logging

sys.path.insert(0,os.path.join(os.path.dirname(__file__),'utils','lib'))

from validate import *
from queries import *

class ArticleHandler(Handler):

	def get(self,article_id):
		
		article = getArticles(int(article_id))
		self.render('article.html',post_title=article.title,
					post_content=article.content,post_id=article.key().id())

