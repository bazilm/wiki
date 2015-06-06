import webapp2
import jinja2
import os

template_path = os.path.join(os.path.dirname(__file__),'templates')
jinja2_environment = jinja2.Environment(loader = jinja2.FileSystemLoader(template_path),
										autoescape=True)

class Handler(webapp2.RequestHandler):

	def write(self,content):
		self.response.write(content)

	def get_template(self,template,*a,**kw):
		t = jinja2_environment.get_template(template)
		return t.render(kw)

	def render(self,template,*a,**kw):
		self.write(self.get_template(template,*a,**kw))

	def render_template(self,template,title="",username="",message=""):
		self.render(template,title=title,username=username,
					message=message)