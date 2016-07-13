default:
	make icons
	gulp
	make html

gulp:
	gulp

gulp-css:
	gulp css
	
gulp-meta:
	gulp meta
	
gulp-icons:
	gulp icons

gulp-images:
	gulp images

html:
	python sources/htmlrender.py --run

icons:
	python sources/buildIcons.py --run