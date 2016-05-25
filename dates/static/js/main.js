function init_map(map_date, latitude, longitude) {
    // this gets the lat and long from the geocoder below
    var var_location = new google.maps.LatLng(latitude, longitude);

    var var_mapoptions = {
        center: var_location,
        zoom: 17
    };

    var var_map = new google.maps.Map(map_date.get(0), var_mapoptions);
    // the zero will get the element the jquery object is wrapping

    var var_marker = new google.maps.Marker({
        position: var_location,
        map: var_map });

    var_marker.setMap(var_map); 
    console.log("Done");
};


$(document).ready(function(){
	console.log("Hi there!")

	$(".button-collapse").sideNav();
    $('.parallax').parallax();
    $('.slider').slider({full_width: true});
    $('select').material_select();

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


//// Register Button ////
    $("#register_button").on('click', function(event){
      event.preventDefault();
      // window.location.replace("/index")

      if (window.location.replace("/index")){
        console.log ("in if")
        var template = $('#register-template').html();
        var renderM = Mustache.render(template, {});
        $('#answer_div').html(renderM);
        window.scrollTo(0, 0);
      }

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


///// Search /////
    $('#nav').on('click', "#search", function(event){
      event.preventDefault();
        var template = $('#search-template').html();
        var renderM = Mustache.render(template, {});
        $('#answer_div').html(renderM);
        window.scrollTo(0, 0);
    });

// Search Button //
    $('#answer_div').on('click', "#search_button", function(event){
      event.preventDefault();
        var template = $('#search-template').html();
        var renderM = Mustache.render(template, {});
        $('#answer_div').html(renderM);
        window.scrollTo(0, 0);
    });


// Category Search Button //
    $('#answer_div').on('click', "#category_search_button", function(event){
    $("#category_search_div").attr("class", "display");
    $("#price_search_div").attr("class", "hide");
    $("#area_search_div").attr("class", "hide");
    });

    $('#answer_div').on('submit', '#category_search_form',function(event){
    event.preventDefault();

    var query_string = $(this).serialize() // returns all the data in your form
    $.ajax({
        method: "POST",
        url: "category",
        data: query_string,
    }).done(function(data, status){

    if (data.success){
      ////// if answers came back ////////
        var template = $('#results-template').html();
        var renderM = Mustache.render(template, {"results":data.results});
        $('#answer_div').html(renderM);
        window.scrollTo(0, 0);
        }
        });
    });


// Price Search Button //
    $('#answer_div').on('click', "#price_search_button", function(event){
    $("#category_search_div").attr("class", "hide");
    $("#price_search_div").attr("class", "display");
    $("#area_search_div").attr("class", "hide");
    });

    $('#answer_div').on('submit', '#price_search_form',function(event){
    event.preventDefault();

    var query_string = $(this).serialize() // returns all the data in your form
    $.ajax({
        method: "POST",
        url: "price",
        data: query_string,
    }).done(function(data, status){

    if (data.success){
      ////// if answers came back ////////
        var template = $('#results-template').html();
        var renderM = Mustache.render(template, {"results":data.results});
        $('#answer_div').html(renderM);
        window.scrollTo(0, 0);
        }
        });
    });


// Area Search Button //
    $('#answer_div').on('click', "#area_search_button", function(event){
    $("#category_search_div").attr("class", "hide");
    $("#price_search_div").attr("class", "hide");
    $("#area_search_div").attr("class", "display");
    });

    $('#answer_div').on('submit', '#area_search_form',function(event){
    event.preventDefault();

    var query_string = $(this).serialize() // returns all the data in your form
    $.ajax({
        method: "POST",
        url: "area",
        data: query_string,
    }).done(function(data, status){

    if (data.success){
      ////// if answers came back ////////
        var template = $('#results-template').html();
        var renderM = Mustache.render(template, {"results":data.results});
        $('#answer_div').html(renderM);
        window.scrollTo(0, 0);
        }
        });
    });


///// Map Display /////
    $('#answer_div').on('submit', ".map_button_form", function(event){
        event.preventDefault();

        var date_id = ($(this).find("[name='date_id']").attr("value")); // find tells it where in the this object to look for the value
        var map_date = $("#" + date_id) // targets the right div in the DOM that has the same post id as our post FK

        var geocoder = new google.maps.Geocoder();
        var address = ($(this).find("[name='address']").attr("value")); // get the address from the DOM of the buttom you clicked

        geocoder.geocode({'address': address}, function(results, status) {
            // this takes the address we got from the DOM and uses google api to get the geocode, then send the geocode to the google maps api
            if (status == google.maps.GeocoderStatus.OK) {
                var latitude = results[0].geometry.location.lat();
                var longitude = results[0].geometry.location.lng();
                // console.log(latitude);
                // console.log(longitude);
                }

            map_date.css({"height":"18em", "margin":"1.2em"});
            init_map(map_date, latitude, longitude);

        }); 
    })

//// Report Button ////
    $('#answer_div').on('click', ".report_button_form", function(event){
    event.preventDefault();
    var report_id = ($(this).find("[name='report_id']").attr("value")); // find tells it where in the this object to look for the value
    $("#" + report_id + 'report_div').attr("class", "display"); // targets the right div in the DOM that has the same id and class combo
    });

    $('#answer_div').on('submit', '#report_form',function(event){
    event.preventDefault();
    var report_id = ($(this).find("[name='report_id']").attr("value")); // find tells it where in the this object to look for the value

    $("#" + report_id + 'report_div').attr("class", "hide");
    $("#" + report_id + 'thanx_div').attr("class", "display");
    });


//// Delete Button ////
    $('#answer_div').on('submit', ".delete_button_form", function(event){
    event.preventDefault();

    var check = confirm("Are you sure you want to delete this date?");

    if (check == true) {
        var delete_id = ($(this).find("[name='delete_id']").attr("value")); // find tells it where in the this object to look for the value

        $.ajax({
            method: "POST",
            url: ("delete/" + delete_id),
            // data: query_string,
        }).done(function(data, status){

            if (data.success){
                ////// if answers came back ////////
                alert("Ok, Date Idea Deleted \nRefresh page to see updated results");
                window.scrollTo(0, 0);
            } else {
                var template = $('#403-template').html();
                var renderM = Mustache.render(template);
                $('#answer_div').html(renderM);  
                window.scrollTo(0, 0);
            }
            });

    } else {
        alert("Ok, Date idea will be kept");
    }
});


//// Vote Up / Like Button ////
    $('#answer_div').on('submit', ".vote_up_button_form", function(event){
    event.preventDefault();

    var check = confirm("Would you like to UP vote this date?");

    if (check == true) {
        var vote_id = ($(this).find("[name='vote_id']").attr("value")); // find tells it where in the this object to look for the value

        $.ajax({
            method: "POST",
            url: ("vote_up/" + vote_id),
            // data: query_string,
        }).done(function(data, status){

            if (data.success){
                ////// if answers came back ////////
                alert("Date UP voted! \nThank you! ");
                window.scrollTo(0, 0);
            } else {
                var template = $('#403-template').html();
                var renderM = Mustache.render(template);
                $('#answer_div').html(renderM);  
                window.scrollTo(0, 0);
            }
            });

    } else {
        alert("Ok, Date idea will be kept");
    }
    });


//// Vote Down Button ////
    $('#answer_div').on('submit', ".vote_down_button_form", function(event){
    event.preventDefault();

    var check = confirm("Would you like to DOWN vote this date?");

    if (check == true) {
        var vote_id = ($(this).find("[name='vote_id']").attr("value")); // find tells it where in the this object to look for the value

        $.ajax({
            method: "POST",
            url: ("vote_down/" + vote_id),
            // data: query_string,
        }).done(function(data, status){

            if (data.success){
                ////// if answers came back ////////
                alert("Date DOWN voted! \nThank you! ");
                window.scrollTo(0, 0);
            } else {
                var template = $('#403-template').html();
                var renderM = Mustache.render(template);
                $('#answer_div').html(renderM);  
                window.scrollTo(0, 0);
            }
            });

    } else {
        alert("Ok, Date idea will be kept");
    }
    });


// Top Dates Button //
    $('#answer_div').on('click', '#top_dates',function(event){
    event.preventDefault();

    $.ajax({
        method: "GET",
        url: "top",
    }).done(function(data, status){

    if (data.success){
      ////// if answers came back ////////
        var template = $('#results-template').html();
        var renderM = Mustache.render(template, {"results":data.results});
        $('#answer_div').html(renderM);
        window.scrollTo(0, 0);
        }
        });
    });

});



