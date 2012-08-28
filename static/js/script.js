$(function() {

	sliding();
// 	showHide();

	// slide up and down items of the sidebar
	function sliding() {
		$('ul.side_nav>ul.subtitel').filter(':nth-child(n+3)').hide()
		
		$('ul.side_nav').on('click', 'li.title', function() {
			$(this)
				.next()
				.slideDown('slow')
				.siblings('ul')
					.slideUp('slow');
		});
	}

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
});
