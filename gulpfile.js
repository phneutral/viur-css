// Project data

var appURL = 'http://www.viur.is';
var appName = 'VIUR CSS';
var appDescription = 'This is the first attempt in building a sturdy foundation of CSS (LESS) for ViUR products and Mausbrand projects. ViUR Ignite CSS is built upon the principles of many CSS guides and frameworks.';

var developerName = 'Mausbrand Infosys';
var developerURL = 'http://mausbrand.de/';

var backgroundColor = '#fff'; // Background color of app icons.

var srcpaths = {
  less: './sources/less/**/*.less',
  images: './sources/images/**/*',
  icons: './sources/icons/**/*',
  meta: './sources/meta/*'
};

var destpaths = {
  css: './appengine/static/css',
  html: './appengine/html',    
  index: './sources/html/_layout.html',
  webfonts: './appengine/static/webfonts',
  images: './appengine/static/images',
  icons: './appengine/static/icons',
  meta: './appengine/static/meta',
};

// Variables and requirements

var gulp = require('gulp');
var rename = require('gulp-rename');

var less = require('gulp-less');
var path = require('path');

var postcss = require('gulp-postcss');
var zindex = require('postcss-zindex');
var autoprefixer = require('gulp-autoprefixer');
var focus = require('postcss-focus');
var nocomments = require('postcss-discard-comments');
var nano = require('gulp-cssnano');

var stylelint = require('stylelint');
var stylelintConfig = require('stylelint-config-standard'); 

var svgmin = require('gulp-svgmin');
var imagemin = require('gulp-imagemin');
var pngquant = require('imagemin-pngquant');

var favicons = require('gulp-favicons');

// compilation and postproduction of LESS to CSS
gulp.task('css', function () {
    var processors = [
    	nocomments, // discard comments
    	focus, // add focus to hover-states
    	zindex, // reduce z-index values
        require('stylelint')(stylelintConfig), // lint the css
        require('postcss-font-magician')({
   			hosted: destpaths.webfonts,
			formats: 'local eot woff2'
		}) // import fonts   
    ];
    return gulp.src('./sources/less/style.less')
        .pipe(less({
      		paths: [ path.join(__dirname, 'less', 'includes') ]
    	})) // compile less to css
        .pipe(autoprefixer({
            browsers: ['last 2 versions'],
            cascade: false
        })) // add vendor prefixes
		.pipe(postcss(processors)) // clean up css
        .pipe(gulp.dest(destpaths.css)) // save cleaned version
        .pipe(nano()) // minify css
        .pipe(rename('style.min.css')) // save minified version 
    	.pipe(gulp.dest(destpaths.css));
});

// reduce images for web
gulp.task ('images', function () {
	return gulp.src(srcpaths.images)
        .pipe(imagemin({
            progressive: true,
            svgoPlugins: [{removeViewBox: false}],
            use: [pngquant()]
        }))
        .pipe(gulp.dest(destpaths.images));
});

gulp.task ('icons', function () {
	return gulp.src(srcpaths.icons)
        .pipe(imagemin({
            progressive: true,
            svgoPlugins: [{removeViewBox: false}],
            use: [pngquant()]
        }))
        .pipe(gulp.dest(destpaths.icons));
});

// crop and resize one meta image to different favicon formats. 
gulp.task ('meta', function () {
    return gulp.src(srcpaths.meta)
		.pipe(favicons({
        appName: appName,
        appDescription: appDescription,
        developerName: developerName,
        developerURL: developerURL,
        background: backgroundColor,
        path: destpaths.meta,
        url: appURL,
        display: "standalone",
        orientation: "portrait",
        version: 1.0,
        logging: false,
        online: false,
        html: destpaths.index,
        replace: true
    	}))
		.pipe(gulp.dest(destpaths.meta));
});

gulp.task('watch', function () {
   gulp.watch(srcpaths.less, ['css']);
   gulp.watch(srcpaths.icons, ['icons']);
   gulp.watch(srcpaths.images, ['images']);
   gulp.watch(srcpaths.meta, ['meta']);
});

gulp.task('default', ['css', 'images', 'icons', 'meta']);