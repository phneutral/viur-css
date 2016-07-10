#! /usr/bin/env python
# -*- coding: utf-8 -*-
from path import path
import operator, os, sys, json, time

reload(sys)
sys.setdefaultencoding("utf-8")

"""	FILE INFO:
	Run this script to render HTML and LESS/CSS

	ALL Rendering
		render.py --all

	HTML Rendering:
		This script grab the content in sources/html and build complete html sites in appengine/html based on _layout.html
		After creating a new html file you have to add the filename and title in the following dict 'sites'[14]
		--html-only
		
	LESS/CSS Rendering:
		This script use gulp to render CSS
		--css-only
"""

__author__ = "Sven Eberth <Sven.Eberth@gmail.com>"



args = sys.argv #get command arguments

if len(args) == 1:
	args.append("--all") # default: all
else:
	if not args[1] in ["--css-only", "--html-only"]:
		sys.exit("Invalid command: %s %s" % (os.path.basename(args[0]), args[1]))



if args[1] == "--css-only" or args[1] == "--all":
	os.system('gulp css')


if args[1] == "--html-only" or args[1] == "--all":
	startTime = time.time()

	with open("html/_sites.json") as json_file: # parse sites
		sites = json.load(json_file)

	sites = sorted(sites.items(), key=operator.itemgetter(1)) # Sort sites by value alphabetically

	layout = open("html/_layout.html", 'r').read() # get Template

	for site, title in sites:
		print ("Processing %s" % site)

		# build navigation
		tmpMenu = '\t\t\t\t' + '<li class="menu-item"><a class="menu-link is-primary' + ( ' is-active' if site == "index.html" else '' ) + '" href="index.html">Start</a></li>' + '\n'
		for siteMenu, titleMenu in sites:
			if siteMenu == "index.html":
				continue
			tmpMenu += '\t\t\t\t' + '<li class="menu-item"><a class="menu-link' + ( ' is-active' if site == siteMenu else '' ) + '" href="' + siteMenu + '">' + titleMenu + '</a></li>' + '\n'
		
		# get content of file
		tmpContent = open("html/" + site, 'r').read()

		# replace variables in template by content
		tmp = layout.replace( '{{title}}', title ).replace( '{{menu}}', tmpMenu ).replace( '{{content}}', tmpContent )

		# write file in appengine/html
		if not os.path.exists("../appengine/html/"):
			os.makedirs("../appengine/html/")

		file = open("../appengine/html/" + site, "w")
		file.write(tmp)
		file.close()

	print "\nFinished 'HTML' after %.2f s" % (time.time() - startTime)
