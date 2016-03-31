# ViUR Ignite CSS #

First attempt in building a sturdy foundation of CSS for ViUR products and Mausbrand projects. 

ViUR Ignite CSS is build upon the principles of: 

* [Primer CSS](http://primercss.io)
* [Enduring CSS](https://benfrain.com/enduring-css-writing-style-sheets-rapidly-changing-long-lived-projects/)
* and others

Thanks guys!

### What is this repository for? ###

* ViUR Ignite CSS is a development toolkit for sturdy HTML and CSS
* It is a lightweighted collection of helpful CSS components
* It is _no_ complete framework
* It is build in LESS

### How do I get set up? ###

* All LESS files are stored in the interface/less folder.
* The function of each LESS file is shown in the according HTML.
* Each LESS file is documented in itself, too.
* style.less is the catalogue of all used less files. Add and remove files as needed.
* Customize your project using appconf.less (for dimensions, fonts and colors) and project.less for custom CSS.
* Only the contents of the appengine folder is deployed to the server.
* Use gulp to compile style.less into the appengine/static/css folder.

### Contribution guidelines ###

* Available for use under the MIT license

### Who do I talk to? ###

* @phneutral