# -*- coding: utf-8 -*-
# vim: set expandtab tabstop=4 shiftwidth=4 :

import imp
import os
import glob
import sys
from byzantium.config import Config
from byzantium.utils import Utils

SYS_PATH_ORIG = [x for x in sys.path]

filters_dir = 'filters_d'	# internally defined filters dir in byzantium.avahi

class Filters(list):
        """ list of AvahiFilter objects """

	def __init__(self):
            """  initialize bits and pieces """
            # load the appropriate config file
	    self.conf = Config('avahi/external_filters.conf')
	    self.utils = Utils()
	    self.logger = self.utils.get_logger()
            # start with an empty list of filters
	    self.all_filters = []
            # collect the filters specified in the config file
	    self.get_all_filters()

	def __contains__(self, item):
            """ Returns True if the filter specified is already in our list
            @param  item    the filter to check for in our list
            @return         True if item is found False if not
            """
	    return self.all_filters.__contains__(item)

	def __missing__(self, item):
            """ Returns True if the filter specified is _not_ already in our list
            @param  item    the filter to check for in our list
            @return         True if item is not found False if it is
            """
	    return self.all_filters.__missing__(item)

	def __getitem__(self, key):
            """ Get the specified filter from the list of filters.
            @param  key     the 
            @return
            """
	    return self.all_filters.__getitem__(key)

	def __iter__(self):
            """ Get an iterable of our list of filters
            @return         iter object of the list of filters
            """
	    return self.all_filters.__iter__()

	def next(self):
            """ Get next filter in the iter object """
	    return self.all_filters.next()

	def __len__(self):
            """ Return the length of our list of filters """
	    return self.all_filters.__len__()

	def count(self, i):
            """  """
	    return self.all_filters.count()

	def index(self, i):
            """  """
	    return self.all_filters.index(i)

	def pop(self, i=-1):
            """  """
	    if len(self.all_filters) > 0 and len(self.all_filters) > i:
	        return self.all_filters[i]
	    else:
	        return None

	def reverse(self):
            """ Return the reverse order of our list of filters """
	    return self.all_filters.reverse()

	def sort(self):
            """ Return a our list of filters sorted """
	    return self.all_filters.sort()

	def _raw_import(self, mod_name):
            """ Import a filter
            @param  mod_name    Name of the module to import
            @return             The imported module if it is found or None if it is not
            """
	    try:
	        mod = __import__(mod_name)
		return mod
	    except ImportError as e:
	        self.logger.error(e)
		return None

	def _try_import(self, mod_name, path=[]):
            """ Attempt to import modules not in the normal import path.
            @param  mod_name    Name of the module to import
            @param  path        list of paths to check for the module in.
            @return             The imported module if it is found or None if it is not
            """
	    have_set_path = False
	    warn_not_found = 'module "%s" not found' % mod_name
	    try:
	        if path and type(path) != list:
		    path = [str(path)]
		if path:
		    have_set_path = True
		    sys.path = path
		    mod = self._raw_import(mod_name)
		    if not mod and have_set_path:
		        sys.path = SYS_PATH_ORIG
			mod = self._raw_import(mod_name)
		    if not mod:
			self.logger.warn(warn_not_found)
			return None
		    return mod
	    finally:
	        sys.path = SYS_PATH_ORIG

	def get_filter_from(self, path='.', mod_name=None, class_name=None):
            """ Get a filter from a specified path using the specified class name
            @param  mod_name    Name of the module to import
            @param  path        list of paths to check for the module in.
            @param class_name   class name to use if mod_name is not the full name of the module
            """
	    self.logger.debug('get_filter_from:\npath: %s\nmodule: %s\nclass: %s' % (path, mod_name, class_name))
	    if path:
	        path_dir = os.path.dirname(path)
		if os.path.isdir(path): path_dir = path
	    else:
		path_dir = None
	    try:
		mod = self._try_import(mod_name, path_dir)
		if mod and class_name:
		    submod = getattr(mod,class_name)
		    if submod: return submod
			return mod
	    except ImportError as e:
	        self.logger.error(e)
		self.logger.warn('module.class "%s.%s" not found' % (mod_name, class_name))
	    return None

	def get_internal_filters(self):
            """ Load default filters """
	    for f in glob.glob(os.path.join(os.path.dirname(__file__), filters_dir)+'/*.py'):
		if not f.endswith('__init__.py'):
		    if not os.path.isdir(f):
		        path = os.path.dirname(f)
		    else:
			path = f
		    mod = os.path.splitext(os.path.basename(f))[0]
		    filter_mod = self.get_filter_from(mod_name=mod, path=path)
	            if filter_mod: self.all_filters.append(filter_mod)

	def get_external_filters(self):
            """ Load filters provided by other systems """
	    self.logger.debug('get_external_filters')
	    external_filters = self.conf.get('avahi/external_filters.d', set_type='config_dir')
	    self.logger.debug(external_filters)
	    if not external_filters or type(external_filters) != list: return None
	    for c in external_filters:
	        self.logger.debug(c.get('filter_path'), c.get('class_name'))
		path = c.get('filter_path')
		self.logger.debug('path', path)
		if path:
		    self.logger.debug('path not empty')
		    module_name = os.path.splitext(os.path.basename(path))[0]
		    class_name = c.get('class_name')
		    self.logger.debug(module_name, class_name, path)
		    if os.path.exists(path):
		        self.logger.debug('path exists')
			try:
			    filter_mod = self.get_filter_from(path, module_name, class_name)
			    self.logger.debug(filter_mod)
			except ImportError as e:
			    self.logger.error(e)
			    filter_mod = None
		if filter_mod:
		    self.all_filters.append(filter_mod)

	def get_all_filters(self):
            """ Get both internal and external filters """
	    self.get_internal_filters()
	    self.get_external_filters()
