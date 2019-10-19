$(document).ready(function(){
	var DOMAIN = "http://"+window.location.hostname;//"http://localhost";

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

		if( $('#sign_in').valid() ) {
		    //submit the form via ajax

			$.ajax({
			url: '/auth/',
			type: 'POST',
			processData: false, // important
            contentType: false, // important
			// pass the form in the FormData constructor to send all the data inside the form
			data: new FormData(this),
			success: function(result) {
					console.log(result);
					if ($.trim(result)=="LOGIN_SUCCESS"){
						swal({
						  type: 'success',
						  title: 'LOGIN SUCCESS',
						  text: 'You have successfully logged in!',
						  showConfirmButton: false,
						  timer: 1000
						},function () {
						setTimeout(function () {
							window.location.href = "../../dashboard.php";
						}, 1500);
						});


					}else if ($.trim(result)=="LOGIN_SUCCESS2"){

						swal({
						  type: 'warning',
						  title: 'LOGIN_SUCCESS2',
						  showConfirmButton: true,
						  timer: 1500
						},function () {
						setTimeout(function () {
							window.location.href = "../../dashboard.php";
						}, 1000);
						});

					}else{


						swal({
						  type: 'error',
						  title: result,
						  showConfirmButton: true

						},function () {
						setTimeout(function () {
							//window.location.href = "?p=home";
						}, 1000);
						});

					}
			},
			error: function(xhr, result, errorThrown){
					swal({
					  type: 'error',
					  title: result,
					  showConfirmButton: true,
					  timer: 1500
					},function () {
					setTimeout(function () {
						//window.location.href = "?p=home";
					}, 1000);
					});
			}
		})

		} else {
		   //show errors
		}

	})









})
