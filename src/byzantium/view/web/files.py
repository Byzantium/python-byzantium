# -*- coding: utf-8 -*-
# vim: set expandtab tabstop=4 shiftwidth=4 :

'''
	Serve files!
'''
import os
import page

class Files(page.Page):
	cType = {
            "png":"images/png",
            "jpg":"images/jpeg",
            "gif":"images/gif",
            "ico":"images/x-icon"
			}
	file_dir = 'files'

	def serve_file(self, name):
		ext = os.path.splitext(name)[-1] # Gather extension
		file_path = os.path.join(self.file_dir, name)
		if os.path.exists(file_path):
			web.header("Content-Type", self.cType[ext] or 'application/octet-stream') # Set content type in header
			return open(file_path, 'rb').read() # Notice 'rb' for reading images
		raise web.not_found()

	def on_GET(self):
		''' example /placeholder '''
		self.set_defaults
		if self.render:
			self.serve_file('/'.join(self.path))
		else:
			raise web.not_found()
		return
