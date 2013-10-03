import shutil
import errno
import os 
import json
import tempfile
import subprocess

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
		
	
		
	def setTemplate(self, page_name, template_filename):
		jsonObj = Json()
		self.writePage(jsonObj.setPageTemplate(page_name, template_filename))

	def createMarkdown(self, page_name, template_block):
		fi, fname = tempfile.mkstemp()
		f = os.fdopen(fi, "w")
		f.write("A First Level Header\n====================\n")
		f.close()
		
		cmd = os.environ.get('VISUAL_EDITOR', 'vi') + ' ' + fname
		subprocess.call(cmd, shell=True)
		
		with open(fname, 'r') as f:
		    print f.read()
		os.unlink(fname)