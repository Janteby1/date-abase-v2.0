$(document).ready(function(){
	console.log("Hi there!")

	$(".button-collapse").sideNav();

	$(document).ready(function(){
    $('.parallax').parallax();
    });


    $('.about').on('click', function(event){ //on click
        event.preventDefault();
		console.log("cool!")

        var template = $('#about-template').html();
        var renderM = Mustache.render(template);
        $('#answer_div').html(renderM);  

    });












});