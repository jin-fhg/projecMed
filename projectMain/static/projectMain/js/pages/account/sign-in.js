$(document).ready(function(){

	var DOMAIN = "http://"+window.location.hostname + ":8000";//"http://localhost";

	$(function () {
		$('#sign_in').validate({
			highlight: function (input) {
				console.log(input);
				$(input).parents('.form-line').addClass('error');
			},
			unhighlight: function (input) {
				$(input).parents('.form-line').removeClass('error');
			},
			errorPlacement: function (error, element) {
				$(element).parents('.input-group').append(error);
			}
		});
	});

	//For Login Part
	$("#sign_in").on("submit",function(e){
		e.preventDefault();
		var uname = $('#username').val();
		var pword = $('#password').val();
        var csrf = $('[name=csrfmiddlewaretoken]').val();

        console.log(uname)
        console.log(pword)
        console.log(csrf)
		if( $('#sign_in').valid() ) {
		    //submit the form via ajax
			$.ajax({
			url: DOMAIN + "/auth/",
			type: 'POST',
			 headers:{
                        "X-CSRFToken": csrf,
                        "username": uname,
                        "password": pword,
                   },
			//dataType: 'json',
			processData: false, // important
            contentType: false, // important
			// pass the form in the FormData constructor to send all the data inside the form
			data: {

                    'username': uname,
                    'password': pword,
                    'csrfmiddlewaretoken': csrf,
			},

			//new FormData(this),
			success: function(data) {
					console.log(data);
					if(data['message'] == "LOGIN_SUCCESS"){
					//if ($.trim(result)=="LOGIN_SUCCESS"){
						swal({
						  type: 'success',
						  title: 'LOGIN SUCCESS',
						  text: 'You have successfully logged in!',
						  showConfirmButton: false,
						  timer: 1000
						},function () {
						setTimeout(function () {
							window.location.href = "/dashboard/";
						}, 1500);
						});


					}else if ($.trim(data)=="LOGIN_SUCCESS2"){

						swal({
						  type: 'warning',
						  title: 'LOGIN_SUCCESS2',
						  showConfirmButton: true,
						  timer: 1500
						},function () {
						setTimeout(function () {
							window.location.href = "/dashboard/";
						}, 1000);
						});

					}else{

						swal({
						  type: 'error',
						  title: data,
						  showConfirmButton: true

						},function () {
						setTimeout(function () {
							window.location.href = "/sign-in/";
						}, 1000);
						});

					}
			},
			error: function(xhr, result, errorThrown){
			        console.log(result);
					swal({
					  type: 'success',
					  title: result,
					  text: 'Login Failed',
					  showConfirmButton: true,
					  timer: 1500
					},function () {
					setTimeout(function () {
						//window.location.href = "/dashboard/";
					}, 1000);
					});
			}
		})

		} else {
		   //show errors
		}

	})








})
