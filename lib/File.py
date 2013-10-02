import shutil
import errno
import os 
import json

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
			
	def createRootPage(self, page_name):
		jsonObj = Json()
		with open('_config/pages.json', 'w') as outfile:
			json.dump(jsonObj.createRootPage(page_name), outfile)