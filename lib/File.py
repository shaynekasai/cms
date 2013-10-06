import shutil
import errno
import os 
import json
import tempfile
import subprocess
import markdown

from Json import Json

from pprint import pprint

class File(object):

	def create(self, destination):
		
		source = "%s/%s" % (os.getcwd(), 'template')
		
		
		try:
			shutil.copytree(source, destination)
		except OSError as exc: # python >2.5
			if exc.errno == errno.ENOTDIR:
				shutil.copy(source, destination)
			else: raise
	
	def writePage(self, str):
		with open('_config/pages.json', 'w') as outfile:
			json.dump(str, outfile)
			
	def createRootPage(self, page_name):
		jsonObj = Json()
		self.writePage(jsonObj.createRootPage(page_name))
		
	def writeMarkdown(self, content, filename):
		with open(filename, 'w') as outfile:
			outfile.write(content)
		outfile.close()
			
	def setTemplate(self, page_name, template_filename):
		jsonObj = Json()
		self.writePage(jsonObj.setPageTemplate(page_name, template_filename))

	def createMarkdown(self, page_name, template_block):
		jsonObj = Json()
		
		fi, fname = tempfile.mkstemp()
		f = os.fdopen(fi, "w")
		f.write("A First Level Header\n====================\n")
		f.close()
		
		cmd = os.environ.get('VISUAL_EDITOR', 'vi') + ' ' + fname
		subprocess.call(cmd, shell=True)
		content = ""
		
		with open(fname, 'r') as f:
		    content = f.read()
		os.unlink(fname)
		
		# search for the page name
		filename = "_content/%s_%s.md" %  (page_name.replace("/", "_"), template_block)
		self.writeMarkdown(content, filename)
		
		
		markdown_block = {template_block:filename}
		self.writePage(jsonObj.setPageMarkdown(page_name, markdown_block))
		
		print filename
		
		# now we need to push this to a file
	
	def build(self, buildType):
		print "Building..."	
		
		json_data = open('_config/pages.json')
		pageConfig = json.load(json_data)
		json_data.close()
		
		
		#loop thru
		currentNode = pageConfig["pages"]["config"]
		self.walkTree(currentNode, "/")
		
		
	def walkTree(self, nodeTree, folder):
		for node in nodeTree:
		
			if folder == "/":
				print "/%s.html" % node["name"]
			else:
				print "%s/%s.html" % (folder, node["name"])
				# create the html page
			
			
			if (node["pages"]):
				# create a folder
				folder = "%s%s" % (folder, node["name"])
				self.walkTree(node["pages"], folder)
	
			