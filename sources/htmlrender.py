#! /usr/bin/env python
# -*- coding: utf-8 -*-
import operator, os, sys, json, time

reload(sys)
sys.setdefaultencoding("utf-8")

"""	FILE INFO:
	This script grab the content in sources/html and build complete html sites in appengine/html based on _layout.html
	After creating a new html file you have to add the filename and title in the dict in html/_sites.json
"""

__author__ = "Sven Eberth <Sven.Eberth@gmail.com>"



htmlDir = "./sources/html/"


def htmlRender():
	startTime = time.time()

	with open(htmlDir+"_sites.json") as json_file: # parse sites
		sites = json.load(json_file)

	sites = sorted(sites.items(), key=operator.itemgetter(1)) # Sort sites by value alphabetically

	layout = open(htmlDir+"_layout.html", 'r').read() # get Template

	for site, title in sites:
		print ("Processing %s" % site)

		# build navigation
		tmpMenu = '<li class="menu-item"><a class="menu-link is-primary' + ( ' is-active' if site == "index.html" else '' ) + '" href="index.html">Start</a></li>' + '\n'
		for siteMenu, titleMenu in sites:
			if siteMenu == "index.html":
				continue
			tmpMenu += '\t\t\t\t' + '<li class="menu-item"><a class="menu-link' + ( ' is-active' if site == siteMenu else '' ) + '" href="' + siteMenu + '">' + titleMenu + '</a></li>' + '\n'
		
		# get content of file
		tmpContent = open(htmlDir+"" + site, 'r').read()

		# replace variables in template by content
		tmp = layout.replace( '{{title}}', title ).replace( '{{menu}}', tmpMenu ).replace( '{{content}}', tmpContent )

		# write file in appengine/html
		if not os.path.exists("./appengine/html/"):
			os.makedirs("./appengine/html/")

		file = open("./appengine/html/" + site, "w")
		file.write(tmp)
		file.close()

	print "\nFinished 'HTML' after %.2f s" % (time.time() - startTime)