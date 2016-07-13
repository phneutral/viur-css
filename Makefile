default:
	python sources/script.py --all
	
gulp:
	python sources/script.py --gulp-only

gulp-css:
	python sources/script.py --gulp-css-only
	
gulp-meta:
	python sources/script.py --gulp-meta-only
	
gulp-icons:
	python sources/script.py --gulp-icons-only

gulp-images:
	python sources/script.py --gulp-images-only

html:
	python sources/script.py --html-only

icons:
	python sources/script.py --icon-less-only