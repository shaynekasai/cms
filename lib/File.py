import shutil
import errno
import os 

class File(object):
		
		
	def create(self, destination):
		
		source = "%s/%s" % (os.getcwd(), 'template')
		
		
		try:
			shutil.copytree(source, destination)
		except OSError as exc: # python >2.5
			if exc.errno == errno.ENOTDIR:
				shutil.copy(source, destination)
			else: raise