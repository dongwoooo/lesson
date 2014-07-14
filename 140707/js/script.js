$(document).ready(function(){
	$('#myModal').modal();

	$('.carousel').carousel();

	$('.dropdown-toggle').dropdown();

	// $('body').scrollspy({ target: '.navbar-example' });
	$( "p" ).clone().appendTo( document.body );
	$( "p" ).clone().appendTo( document.body );
	$( "p" ).clone().appendTo( document.body );
	$(window).scroll(function(){
		$("span, #1st").css( "display", "inline" ).fadeOut('fast');
	});
});