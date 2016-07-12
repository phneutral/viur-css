#! /usr/bin/env python
# -*- coding: utf-8 -*-
import operator, os, sys, json, time
from sources.htmlrender import htmlRender
from sources.buildIcons import iconlessRender

reload(sys)
sys.setdefaultencoding("utf-8")

"""	FILE INFO:
	Run this script to render HTML, GULP and build icon classes

	ALL Rendering
		script.py --all or only script.py

	HTML Rendering:
		This script grab the content in sources/html and build complete html sites in appengine/html based on _layout.html
		After creating a new html file you have to add the filename and title in the dict in sources/html/_sites.json
		--html-only

	ICON LESS Rendering:
		This script build the Before-Classes in sources/icon.less for each icon in sources/icons
		The class will be written at the end of icon.less
		--icon-less-only
		
	GULP Rendering:
		This command start gulp
		--gulp-only

		Subcommands:
			--gulp-images-only
			--gulp-css-only
			--gulp-icons-only
			--gulp-meta-only
"""

__author__ = "Sven Eberth <Sven.Eberth@gmail.com>"



args = sys.argv #get command arguments

if len(args) == 1:
	args.append("--all") # default: all
else:
	if not args[1] in ["--all", "--html-only", "--gulp-only", "--gulp-css-only", "--gulp-meta-only", "--gulp-icons-only", "--gulp-images-only", "--icon-less-only"]:
		sys.exit("Invalid command: %s %s" % (os.path.basename(args[0]), args[1]))



if args[1] == "--icon-less-only" or args[1] == "--all":
	iconlessRender()
if args[1] == "--gulp-only" or args[1] == "--all":
	os.system('gulp')
if args[1] == "--gulp-css-only":
	os.system('gulp css')
if args[1] == "--gulp-meta-only":
	os.system('gulp meta')
if args[1] == "--gulp-icons-only":
	os.system('gulp icons')
if args[1] == "--gulp-images-only":
	os.system('gulp images')
if args[1] == "--html-only" or args[1] == "--all":
	htmlRender()