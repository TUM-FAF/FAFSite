$(function() {
	$('ul.side_nav>ul.subtitel').filter(':nth-child(n+3)').hide()
	
	$('ul.side_nav').on('click', 'li.title', function() {
		console.log( $(this).next() );
		$(this)
			.next()
			.slideDown('slow')
			.siblings('ul')
				.slideUp('slow');
	});
}); 