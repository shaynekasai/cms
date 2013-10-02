import json

class Json(object):
	def __init__(self):
		json_data = open('_config/pages.json')
		self.pageConfig = json.load(json_data)
		json_data.close()
		
	
	def createRootPage(self, page_name):
		
		self.pageConfig["pages"]["config"].append({"name": page_name, "template":"", "content":[]})
		
		
		return self.pageConfig
		
	def createChildPage(self):
		print "Creating a child page"
		
	def setPageTemplate(self):
		print "Setting the template for a page"