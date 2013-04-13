$(document).ready(function() {

sliding('courses');
sliding('people');

// slide up and down items of the sidebar on the courses page
function sliding(page) {
	if (page == 'courses') {
		$('ul.side_nav.courses>ul.subtitel').find('.active').closest('ul').siblings('ul').hide(); 
	}
	else if (page == 'people') {
		var non_active = $('ul.side_nav.people>ul.subtitel').find('.active').closest('ul').siblings('ul')
		if (non_active.length == 0) {
			non_active = $('ul.side_nav.people>ul.subtitel');
		}
		non_active.hide()
	}
	
	$('ul.side_nav').on('click', 'li.title', function() {
		$(this)
			.next()
			.slideDown('slow')
			.siblings('ul')
				.slideUp('slow');
	});
}

// show and hide the ID cards
$tbody = $('body');
var people = {
	init: function(){
		 $tbody.find('tr.person').unbind().click(function(){
			$this = $(this);
			people.hide('all');
			people.show('all');
			$this.hide().next().show();
			 $tbody
				.find('tr.id_card .hide_btn').click(function(){
					$(this)
						.parents('tr.id_card').hide();
					people.show('all');
				 })
		});
	},
	hide: function(val){
		if(val == 'all')
			$tbody.find('tr.id_card').hide();
		else
			val.hide();
	},
	show: function(val){
		if(val == 'all')
			$tbody.find('tr.person').show();
		else
			val.show();
	}
};
people.hide('all');
people.init();


// Handle timeline on blog pages of activities and achievements
var Timeline = Object();

Timeline.init = function init(val) {
	var first = 0, 
		second = 0,
		left = 0,
		right = 0;
	var id = 1;
	var main = $('.timeline_main');
	var articles = main.find('#articles');

	articles.each(function() {
		var article = $(this);
		article.find('article').attr('data-id', id);
		id++;
		article.removeClass('right')
			.removeClass('left')
			.removeClass('first')
			.removeClass('second');

		if(!first) {
			article.addClass('left').addClass('first');
			first = 1;
			left += article.outerHeight();
		}
		else {
			if(!second) {
				article.addClass('right').addClass('second');
				second = 1;
				right+=article.outerHeight();
			}
			else {
				if(left <= right) {
					article.addClass('left');
					left+=article.outerHeight();
				}
				else {
					article.addClass('right');
					right+=article.outerHeight();
				}
			}
		}
		if(val != 1) {
			article.removeClass('long');
		} else {
			if(article.hasClass('long')) {
				left = 0;
				right = 0;
				article.removeClass('second').removeClass('right').removeClass('left');
			}
		}
		if(article.hasClass('first') && article.hasClass('long')) {
			second = 1;
			left = 0;
		}
	});
};

Timeline.expand_article = function expand_article() {
	$('a.read_more').click(function(e) {
		e.preventDefault();

		// c($('#content'));
		// $('#content').each(function() {
		// 	c($(this));
		// 	$(this).hide();
		// });

		// $('.preview').each(function() {
		// 	// c($(this));
		// 	$(this).show();
		// })
		
		var article_id = $(this).parents('article').attr('data-id');
		window.location.hash = article_id;
		Timeline.init();
		var section = $(this).parents('section');
		var preview = $(this).parents('#preview');
		$(preview).hide();
		var content = $(this).parents('.article_body').children('#content');
		$(section).removeClass('right')
					.removeClass('left')
					.removeClass('second')
					.addClass('long');
		$(content).show();
		Timeline.init(1);
		var position = $(section).position().top + $(section).parent().position().top 
			- $(window).height()/2 + $(section).outerHeight()/2 +20;
		$('body').delay(100).animate({scrollTop: position}, 1000);
	});
};

Timeline.shrink_article = function shrink_article() {
	$('a.hide_btn').click(function(e) {
		e.preventDefault();
		history.pushState("", document.title, window.location.pathname);
		var section = $(this).parents('section');
		var content = $(this).parents('.article_body').children('#content');
		var preview = $(this).parents('.article_body').children('#preview');
		$(content).hide();
		$(preview).show();
		$(section).removeClass('right')
					.removeClass('left')
					.removeClass('second')
					.removeClass('long');
		Timeline.init();
	});
}

Timeline.hash = function hash() {
	var $hash = window.location.hash;
	$hash = $hash.substring(1);
	if($hash.length > 0) {
		$('[data-id="'+$hash+'"]').find('a.read_more').click();
		Timeline.init(1);
	} 
};

Timeline.init();
Timeline.expand_article();
Timeline.shrink_article();
Timeline.hash();

function c(val) {
	console.log(val);
}

});
