#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys

"""	FILE INFO:
	This script build the Before-Classes in icon.less for each icon in @iconDir
	The class will be written at the end of file
"""

__author__ = "Sven Eberth <Sven.Eberth@gmail.com>"



iconDir = "./sources/icons"
lessDir = "./sources/less"



def iconlessRender(folder=""):
	_iconless = open(lessDir+"/icon_prototype.less", 'r').read() # get _less file 

	file = open(lessDir+"/icon.less", "w") # write start of _less file
	file.write("/* ALL CHANGES IN THIS WILL BE OVERWRITTEN */\n/* USE icon_prototype.less */\n\n\n" + _iconless)
	file.close()
	writeClasses(folder)
	

def writeClasses(folder=""):
	file = open("sources/less/icon.less", "a")

	for item in os.listdir(iconDir+folder): # for each item in folder
		
		if os.path.isdir(iconDir+"/"+folder+item): # if dir
			writeClasses(folder+"/"+item)
		else: # if file
			print ("Processing %s" % folder+"/"+item)

			tmpClass = ".i-"+item.replace('.svg','').replace(' ', '-')
			tmpLess  =	tmpClass+":before {" +"\n"
			tmpLess +=		"\tbackground-image:url('../icons"+folder+"/"+item+"');" +"\n"
			tmpLess +=	"}"+"\n";
	
			file.write(tmpLess)
	file.close()