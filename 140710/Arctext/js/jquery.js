$(document).ready(function(){
	$('p.top').arctext({radius: 1000, dir: 1});
	$('p.bottom').arctext({radius: 1000, dir: -1});
	$('body').on('click', function() {
		$('p.top').arctext('set', {
			radius		: 1000, 
			dir			: -1, 
			animation	: {
				speed	: 300
			}
		});
		$('p.bottom').arctext('set', {
			radius		: 1000, 
			dir			: 1, 
			animation	: {
				speed	: 300
			}
		});
		return false;
	});
	$('body').click(function(){
		$('.closed').fadeOut('300');
		$('.opened').delay('300').fadeIn('300');
	})
});