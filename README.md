# ViUR Ignite CSS #

This is the first attempt in building a sturdy foundation of CSS (LESS) for ViUR products and Mausbrand projects.
ViUR Ignite CSS is built upon the principles of many CSS guides and frameworks.

Different projects demand different solutions.
ViUR Ignite CSS is a solution based on the needs of our python/jinja oriented stack.
A lightweight framework for many different customer projects.
For other purposes you may use one of the frameworks or guides below.
Their samples, knowledge and expertise helped us to make ViUR Ignite CSS.

* [Primer CSS](http://primercss.io)
* [Enduring CSS](https://benfrain.com/enduring-css-writing-style-sheets-rapidly-changing-long-lived-projects/)
* [Bulma](http://bulma.io)
* [CSS Guidelin.es](http://cssguidelin.es)
* [Bijou](http://andhart.github.io/bijou)
* [Bedrock](https://github.com/jscarmona/bedrock)
* and others

Thanks guys!

### What is this repository for? ###

* ViUR Ignite CSS is a development toolkit for sturdy HTML and CSS
* It is a lightweightned collection of helpful CSS components
* It is responsive and adaptable
* It is build in LESS
* ViUR Ignite CSS is JavaScript free as most projects use their own JS implementation.

### How do I get set up? ###

* All LESS files are stored in the sources/less folder.
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