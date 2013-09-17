#!/usr/bin/env python

from distutils.core import setup

setup(
	name='Byzantium',
	version='2013.09.17',
	author='haxwithaxe',
	author_email='me@haxwithaxe.net',
	url='http://project-byzantium.org/',
	description='',
	long_description='',
	download_url='https://github.com/Byzantium/python-byzantium',
	package_dir={
		'':'src',
		'byzantium':'src/byzantium',
		'avahi':'src/byzantium/avahi',
        'view':'src/byzantium/view',
        'web':'src/byzantium/view/web',
		},
	packages=[
		'byzantium',
		'byzantium.avahi',
		'byzantium.avahi.filters_d',
		'byzantium.view',
		'byzantium.view.web'
		],
	classifiers=[
		'Development Status :: Beta',
		'Environment :: Console',
		'Environment :: Web Environment',
		'Intended Audience :: Developers',
		'Intended Audience :: System Administrators',
		'License :: OSI Approved :: GPLv3',
		'Operating System :: POSIX',
		'Programming Language :: Python',
		'Topic :: System Administration',
		'Topic :: Networking :: Mesh',
		'Topic :: Software Development :: Services',
		],
	license='GPLv3',
	requires=['dbus','pykka','web', 'gobject', 'avahi']
	)

