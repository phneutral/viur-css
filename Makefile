default:
	make css
	make js
	make html

all:
	make iconClass
	gulp
	make html

gulp:
	gulp

js:
	gulp js

css:
	gulp css
	
meta:
	gulp meta
	
icons:
	gulp icons

images:
	gulp images

html:
	python sources/htmlrender.py --run

iconClass:
	python sources/buildIcons.py --run