$(function() {
	$('ul.side_nav>ul.semester_courses').filter(':nth-child(n+3)').hide()
	
	$('ul.side_nav').on('click', 'li.semester_number', function() {
		console.log( $(this).next() );
		$(this)
			.next()
			.slideDown('slow')
			.siblings('ul')
				.slideUp('slow');
	});
}); 