import json

class Json(object):
	def __init__(self):
		json_data = open('_config/pages.json')
		self.pageConfig = json.load(json_data)
		json_data.close()
		
	
	def createRootPage(self, page_name):
		
		self.pageConfig["pages"]["config"].append({"name": page_name, "template":"", "content":[], "pages":[]})
		
		
		return self.pageConfig
		
	def createChildPage(self):
		print "Creating a child page"
		
	def setPageTemplate(self, page_name, template_filename):
		print "Setting the template for %s" % page_name
		nodePath = page_name.split("/")
		
		
		currentNode = self.pageConfig["pages"]["config"]
		lastNode = None
		
		for path in nodePath:
			for node in currentNode:
				if node["name"] == path:
					lastNode = node
					currentNode = node["pages"]
		
		lastNode["template"] = template_filename
					
		return self.pageConfig