$(document).ready(function() {
	// fix menu when passed
	$('.masthead')
		.visibility({
			once: false,
			onBottomPassed: function() {
				$('.fixed.menu').transition('fade in');
			},
			onBottomPassedReverse: function() {
				$('.fixed.menu').transition('fade out');
			}
		})
	;

	// create sidebar and attach to menu open
	$('.ui.sidebar').sidebar('attach events', '.toc.item', 'overlay');
	
});
$(document).on('click', ".contacto", function(e){
	e.preventDefault();
	$(".ui.sidebar").sidebar("hide");
	$('html,body').animate({scrollTop: $('#contacto').offset().top * .98},'fast');
});