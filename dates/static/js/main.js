$(document).ready(function(){
	console.log("Hi there!")

	$(".button-collapse").sideNav();
    $('.parallax').parallax();
    $('.slider').slider({full_width: true});

// goes to top of page on reload
$( window ).unload(function() {
  window.scrollTo(0, 0);
    console.log("again")
});


///// About /////
    $('#nav').on('click', "#about", function(event){
        event.preventDefault();

        var template = $('#about-template').html();
        var renderM = Mustache.render(template);
        $('#answer_div').html(renderM);  

    });


///// Register /////
    $('#nav').on('click', "#register", function(event){
      event.preventDefault();
        var template = $('#register-template').html();
        var renderM = Mustache.render(template, {});
        $('#answer_div').html(renderM);
        window.scrollTo(0, 0);
    });

    $('#answer_div').on('submit', '#register_form',function(event){
    event.preventDefault();

    var query_string = $(this).serialize() // returns all the data in your form
    $.ajax({
        method: "POST",
        url: "register",
        data: query_string,
    }).done(function(data, status){
    // console.log(data.Message)

    if (data.success){
      ////// if they registered then display the Login ////////
            var template = $('#login-template').html();
            var renderM = Mustache.render(template, {});
            $('#answer_div').html(renderM);
            window.scrollTo(0, 0);
            // $('#answer_div').append(data.Message);
            }
      else {
        // console.log (data.errors)
        var template = $('#register-template').html();
        var renderM = Mustache.render(template, data.errors);
        $('#answer_div').html(renderM);
        window.scrollTo(0, 0);
      }

        });
    });


/////// Login /////
    $('#nav').on('click', "#login", function(event){
      event.preventDefault();
        var template = $('#login-template').html();
        var renderM = Mustache.render(template, {'id_username':'account_circle','id_password':'verified_user'});
        $('#answer_div').html(renderM);
        window.scrollTo(0, 0);
    });

    $('#answer_div').on('submit', '#login_form',function(event){
      event.preventDefault();

      var query_string = $(this).serialize() //returns all the data in your form
      // console.log(query_string)

      $.ajax({
          method: "POST",
          url: "login",
          data: query_string,
      }).done(function(data, status){
        
          if (data.success){
          ////// if they login correctly ////////
            console.log("HERE")
            document.location.href="/index";
            window.scrollTo(0, 0);
          } 
          else{
            // crazy code to select for the error formating
            var template = $('#login-template').html();
            var errorNames = Object.keys(data.errors).reduce(function(previousValue, currentValue, currentIndex, array){
              return (previousValue ? previousValue + ',':'') + 'input[name="'+currentValue+'"]'
            }, '');
            var renderM = Mustache.render(template, $.extend(data.errors,{'id_username':'account_circle','id_password':'verified_user'}));
            $('#answer_div').html(renderM);


            var inputs = $('#login_form').find(errorNames);
            inputs.addClass('invalid');
            $.each(inputs, function(idx, el){
              $($(el).next()).css("white-space", "nowrap");
              $($(el).next()).css("overflow", "hidden;");
            });

            // prints errors that are not missing fields to the end of the form
            $('.tall .container').append(data.errors["__all__"][0]);
            $('.tall .container').css("color", "red");

            window.scrollTo(0, 0);
          }

      });
    });


///// Logout /////
    $('#nav').on('click', "#logout", function(event){
    event.preventDefault();

    // var query_string = $(this).serialize() // returns all the data in your form

    $.ajax({
        method: "POST",
        url: "logout",
        // data: query_string,
    }).done(function(data, status){

    // $('#answer_div').html(" <h2> Goodbye, See you soon!</h2>");
    document.location.href="/";
    window.scrollTo(0, 0);

    });
});


///// Create /////
    $('#nav').on('click', "#add", function(event){
        event.preventDefault();

        var template = $('#create-template').html();
        var renderM = Mustache.render(template);
        $('#answer_div').html(renderM);  
        window.scrollTo(0, 0);
    });


    $('#answer_div').on('submit', '#create_form',function(event){
    event.preventDefault();

    var query_string = $(this).serialize() //returns all the data in your form
    console.log(query_string)

    $.ajax({
        method: "POST",
        url: "add",
        data: query_string,
    }).done(function(data, status){

    if (data.success){
        console.log(data.Message)
        var template = $('#thanx-template').html();
        var renderM = Mustache.render(template);
        $('#answer_div').html(renderM);  
        window.scrollTo(0, 0);
        }
    else {
        var template = $('#403-template').html();
        var renderM = Mustache.render(template);
        $('#answer_div').html(renderM);  
        window.scrollTo(0, 0);
        }

        });
    });






});