$(function() {
	$('.js-codeMe').each(function() {
		var html = $(this).outerHTML().replace(' js-codeMe', '')
		var escaped = $("<div>").text(html).html();
		console.log(html);

		$(this).after('<pre class="brush: html">'+escaped+'</pre>');
		SyntaxHighlighter.highlight()
	})
})