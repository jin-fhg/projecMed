$(document).ready(function(){
	var DOMAIN = "http://localhost";
	$("#register_form").on("submit",function(){
		var status_fname = false;
		var status_email = false;
		var status_pass1 = false;
		var status_pass1 = false;
		var status_type = false;
		var fname = $("#fname");
		var email = $("#email");
		var pass1 = $("#password1");
		var pass2 = $("#password2");
		var type = $("#usertype");
		//
		var e_patt = new RegExp(/^[a-z0-9_-]+(\.[a-z0-9_-]+)*@[a-z0-9_-]+(\.[a-z0-9_-]+)*(\.[a-z]{2,4})$/);
		
		if(fname.val() == "" || fname.val().length < 2){
			fname.addClass("border-danger");
			$("#fname_error").html("<span class='text-danger'>Please Enter Name and Name should be more than 2 char</span>");
			status_fname = false;
		}else{
			fname.removeClass("border-danger");
			$("#fname_error").html("");
			status_fname = true;
		}

		
		if(email.val() == "" || !e_patt.test(email.val())){
			email.addClass("border-danger");
			$("#email_error").html("<span class='text-danger'>Please Enter Valid Email Address</span>");
			status_email = false;
		}else{
			email.removeClass("border-danger");
			$("#email_error").html("");
			status_email = true;
		}
		if(pass1.val() == "" || pass1.val().length < 9){
			pass1.addClass("border-danger");
			$("#p1_error").html("<span class='text-danger'>Please Enter more than 9 digit password</span>");
			status_pass1 = false;
		}else{
			pass1.removeClass("border-danger");
			$("#p1_error").html("");
			status_pass1 = true;
		}
		if(pass2.val() == "" || pass2.val().length < 9){
			pass2.addClass("border-danger");
			$("#p2_error").html("<span class='text-danger'>Please Enter more than 9 digit password</span>");
			status_pass2 = false;
		}else{
			pass2.removeClass("border-danger");
			$("#p2_error").html("");
			status_pass2 = true;
		}
		if(type.val() == ""){
			type.addClass("border-danger");
			$("#t_error").html("<span class='text-danger'>Please Enter more than 9 digit password</span>");
			status_type = false;
		}else{
			type.removeClass("border-danger");
			$("#t_error").html("");
			status_type = true;
		}
		if ((pass1.val() == pass2.val()) && 
		status_fname == true && 
		status_email == true && 
		status_pass1 == true && 
		status_pass2 == true && 
		status_type == true) {
			$(".overlay").show();
			$.ajax({
				url : DOMAIN+"/includes/process.php",
				method : "POST",
				data : $("#register_form").serialize(),
				success : function(data){
					if (data == "EMAIL_ALREADY_EXISTS") {
						$(".overlay").hide();
						alert("It seems like you email is already used");
					}else if(data == "SOME_ERROR"){
						$(".overlay").hide();
						alert("Something Wrong");
					}else{
						$(".overlay").hide();
						window.location.href = encodeURI(DOMAIN+"/index.php?msg=You are registered Now you can login");
					}
				}
			})
		}else{
			pass2.addClass("border-danger");
			$("#p2_error").html("<span class='text-danger'>Password is not matched</span>");
			status = true;
		}
	})

	//For Login Part
	$("#form_login").on("submit",function(){
		var email = $("#log_email");
		var pass = $("#log_password");
		var status = false;
		if (email.val() == "") {
			email.addClass("border-danger");
			$("#e_error").html("<span class='text-danger'>Please Enter Email Address</span>");
			status = false;
		}else{
			email.removeClass("border-danger");
			$("#e_error").html("");
			status = true;
		}
		if (pass.val() == "") {
			pass.addClass("border-danger");
			$("#p_error").html("<span class='text-danger'>Please Enter Password</span>");
			status = false;
		}else{
			pass.removeClass("border-danger");
			$("#p_error").html("");
			status = true;
		}
		if (status) {
			$(".overlay").show();
			$.ajax({
				url : DOMAIN+"/includes/process.php",
				method : "POST",
				data : $("#form_login").serialize(),
				success : function(data){
					if ($.trim(data) == "NOT_REGISTERD") {
						$(".overlay").hide();
						email.addClass("border-danger");
						$("#e_error").html("<span class='text-danger'>It seems like you are not registered</span>");
					}else if($.trim(data) == "PASSWORD_NOT_MATCHED"){
						$(".overlay").hide();
						pass.addClass("border-danger");
						$("#p_error").html("<span class='text-danger'>Please Enter Correct Password</span>");
						status = false;
					}else if ($.trim(data)=="USER_LOCKED"){
					alert("ACCOUNT LOCKED!. Please Contact System Administrator");
					window.location.href = "login.php";
					}else{
						$(".overlay").hide();
						console.log(data);
						window.location.href = DOMAIN+"/?p=home";
					}
				}
			})
		}
	})

	//Fetch category
	fetch_category();
	function fetch_category(){
		$.ajax({
			url : DOMAIN+"/includes/process.php",
			method : "POST",
			data : {getCategory:1},
			success : function(data){
				var root = "<option value='0'>Root</option>";
				var choose = "<option value=''>Choose Category</option>";
				$("#parent_cat").html(root+data);
				$("#select_cat").html(choose+data);
			}
		})
	}

	//Fetch Brand
	fetch_brand();
	function fetch_brand(){
		$.ajax({
			url : DOMAIN+"/includes/process.php",
			method : "POST",
			data : {getBrand:1},
			success : function(data){
				var choose = "<option value=''>Choose Brand</option>";
				$("#select_brand").html(choose+data);
			}
		})
	}

	//Add Category
	$("#category_form").on("submit",function(){
		if ($("#category_name").val() == "") {
			$("#category_name").addClass("border-danger");
			$("#cat_error").html("<span class='text-danger'>Please Enter Category Name</span>");
		}else{
			$.ajax({
				url : DOMAIN+"/includes/process.php",
				method : "POST",
				data  : $("#category_form").serialize(),
				success : function(data){
					if (data == "CATEGORY_ADDED") {
							$("#category_name").removeClass("border-danger");
							$("#cat_error").html("<span class='text-success'>New Category Added Successfully..!</span>");
							$("#category_name").val("");
							fetch_category();
					}else{
						alert(data);
					}
				}
			})
		}
	})


	//Add Brand
	$("#brand_form").on("submit",function(){
		if ($("#brand_name").val() == "") {
			$("#brand_name").addClass("border-danger");
			$("#brand_error").html("<span class='text-danger'>Please Enter Brand Name</span>");
		}else{
			$.ajax({
				url : DOMAIN+"/includes/process.php",
				method : "POST",
				data : $("#brand_form").serialize(),
				success : function(data){
					if (data == "BRAND_ADDED") {
						$("#brand_name").removeClass("border-danger");
						$("#brand_error").html("<span class='text-success'>New Brand Added Successfully..!</span>");
						$("#brand_name").val("");
						fetch_brand();
					}else{
						alert(data);
					}
						
				}
			})
		}
	})

	//add product
	$("#product_form").on("submit",function(){
		$.ajax({
				url : DOMAIN+"/includes/process.php",
				method : "POST",
				data : $("#product_form").serialize(),
				success : function(data){
					if (data == "NEW_PRODUCT_ADDED") {
						alert("New Product Added Successfully..!");
						$("#product_name").val("");
						$("#select_cat").val("");
						$("#select_brand").val("");
						$("#product_price").val("");
						$("#product_qty").val("");

					}else{
						console.log(data);
						alert(data);
					}
						
				}
			})
	})

	//add product
	

	$("#labreport_form").submit(function(e){
		// prevent the form from submitting
		e.preventDefault();
		$.ajax({
			url: DOMAIN+"/includes/process.php",
			type: 'POST',
			processData: false, // important 
            contentType: false, // important
			// pass the form in the FormData constructor to send all the data inside the form
			data: new FormData(this),
			success: function(result) {

					if ($.trim(result) == "LABREPORT_ADDED"){
						
					Swal({
					  type: 'success',
					  title: 'LAB REPORT Added Successfully!.',
					  showConfirmButton: false,
					  timer: 1500
					}).then(function() {
					window.location.reload();
					});	
						
					}else{
						console.log(result);
						
					Swal({
					  type: 'error',
					  title: result,
					  showConfirmButton: true,
					  timer: 1500
					}).then(function() {
					//window.location.reload();
					});	
					
					}

			},
			error: function(xhr, result, errorThrown){
					Swal({
					  type: 'error',
					  title: 'Request Failed!',
					  showConfirmButton: true,
					  timer: 1500
					}).then(function() {
					//window.location.reload();
					});	
			}
		});
		//$('#picture').val('');
		//$('#body').val('');
	})
		
	$("#addappointment_form").submit(function(e){
		// prevent the form from submitting
		e.preventDefault();
				$("#BTNaddappointment_form").attr("disabled", true);
		$.ajax({
			url: DOMAIN+"/includes/process.php",
			type: 'POST',
			processData: false, // important 
            contentType: false, // important
			// pass the form in the FormData constructor to send all the data inside the form
			data: new FormData(this),
			success: function(result) {
				if ($.trim(result)=="EMAIL_ALREADY_EXISTS"){
				//alert(result);

					Swal({
					  type: 'warning',
					  title: 'EMAIL ALREADY EXIST!.',
					  showConfirmButton: true,
					  //timer: 1500
					}).then(function() {
					//window.location.reload();
					});	
					
				}else if ($.trim(result)=="Appointment Successfully Added!"){
					
					Swal({
					  type: 'success',
					  title: "APPOINTMENT SUCCESSFULLY ADDED!",
					  showConfirmButton: false,
					  timer: 1500
					}).then(function() {
					window.location.reload();
					});	
					
				}else{
					
					Swal({
					  type: 'error',
					  title: result,
					  showConfirmButton: true,
					  //timer: 1500
					}).then(function() {
					//window.location.reload();
					});	
					
				}
						$("#BTNaddappointment_form").attr("disabled", false);
			},
			error: function(xhr, result, errorThrown){
					Swal({
					  type: 'error',
					  title: "Request Failed!",
					  showConfirmButton: true,
					  timer: 1500
					}).then(function() {
					//window.location.reload();
					});	
							$("#BTNaddappointment_form").attr("disabled", false);
			}
		});
		//$('#picture').val('');
		//$('#body').val('');
	})
		
	
		$("#medcert_form").submit(function(e){
		// prevent the form from submitting
		e.preventDefault();
		$.ajax({
			url: DOMAIN+"/includes/process.php",
			type: 'POST',
			processData: false, // important 
            contentType: false, // important
			// pass the form in the FormData constructor to send all the data inside the form
			data: new FormData(this),
			success: function(result) {
				if ($.trim(result)=="medcert_success"){
				
					Swal({
					  type: 'success',
					  title: "MEDICAL CERTIFICATE SUCCESSFULLY ADDED!",
					  showConfirmButton: false,
					  timer: 1500
					}).then(function() {
					window.location.reload();
					});	
					
				}else{
					
					Swal({
					  type: 'error',
					  title: result,
					  showConfirmButton: true,
					  //timer: 1500
					}).then(function() {
					//window.location.reload();
					});	
					
				}	

				},
			error: function(xhr, result, errorThrown){
			
					Swal({
					  type: 'error',
					  title: result,
					  showConfirmButton: true,
					  //timer: 1500
					}).then(function() {
					//window.location.reload();
					});	
				}
		});
		//$('#picture').val('');
		//$('#body').val('');
	})
		
		$("#medclearance_form").submit(function(e){
		// prevent the form from submitting
		e.preventDefault();
		$.ajax({
			url: DOMAIN+"/includes/process.php",
			type: 'POST',
			processData: false, // important 
            contentType: false, // important
			// pass the form in the FormData constructor to send all the data inside the form
			data: new FormData(this),
			success: function(result) {

				if ($.trim(result)=="medclearance_success"){
				
					Swal({
					  type: 'success',
					  title: "MEDICAL CLEARANCE SUCCESSFULLY ADDED!",
					  showConfirmButton: false,
					  timer: 1500
					}).then(function() {
					window.location.reload();
					});	
					
				}else{
					
					Swal({
					  type: 'error',
					  title: result,
					  showConfirmButton: true,
					  //timer: 1500
					}).then(function() {
					//window.location.reload();
					});	
					
				}

			},
			error: function(xhr, result, errorThrown){

					Swal({
					  type: 'error',
					  title: result,
					  showConfirmButton: true,
					  //timer: 1500
					}).then(function() {
					//window.location.reload();
					});	


				//alert('Request failed.');
			}
		});
		//$('#picture').val('');
		//$('#body').val('');
	})
		$("#CreatePaymentProcedure").submit(function(e){
		// prevent the form from submitting
		e.preventDefault();
		$.ajax({
			url: DOMAIN+"/includes/process.php",
			type: 'POST',
			processData: false, // important 
            contentType: false, // important
			// pass the form in the FormData constructor to send all the data inside the form
			data: new FormData(this),
			success: function(result) {
		//		alert(result);
	//			window.location.reload();
				
				if ($.trim(result)=="CreatePaymentProcedure_added"){
					
					Swal({
					  type: 'success',
					  title: "Payment Procedure Successfully Added!",
					  showConfirmButton: false,
					  timer: 1500
					}).then(function() {
					window.location.reload();
					});	
					
				}else{
					
					Swal({
					  type: 'error',
					  title: result,
					  showConfirmButton: true,
					  //timer: 1500
					}).then(function() {
					//window.location.reload();
					});	
					
				}				
				
				
				
			},
			error: function(xhr, result, errorThrown){
					Swal({
					  type: 'error',
					  title: result,
					  showConfirmButton: true,
					  //timer: 1500
					}).then(function() {
					//window.location.reload();
					});	
			}
		});
		//$('#picture').val('');
		//$('#body').val('');
	})		
		$("#text_form").submit(function(e){
		// prevent the form from submitting
		e.preventDefault();
		$.ajax({
			url: DOMAIN+"/includes/process.php",
			type: 'POST',
			processData: false, // important 
            contentType: false, // important
			// pass the form in the FormData constructor to send all the data inside the form
			data: new FormData(this),
			success: function(result) {
		//		alert(result);
	//			window.location.reload();
				
				if ($.trim(result)=="text_added"){
					
					Swal({
					  type: 'success',
					  title: "SUCCESSFULLY ADDED!",
					  showConfirmButton: false,
					  timer: 1500
					}).then(function() {
					window.location.reload();
					});	
					
				}else{
					
					Swal({
					  type: 'error',
					  title: result,
					  showConfirmButton: true,
					  //timer: 1500
					}).then(function() {
					//window.location.reload();
					});	
					
				}				
				
				
				
			},
			error: function(xhr, result, errorThrown){
					Swal({
					  type: 'error',
					  title: result,
					  showConfirmButton: true,
					  //timer: 1500
					}).then(function() {
					//window.location.reload();
					});	
			}
		});
		//$('#picture').val('');
		//$('#body').val('');
	})
		
		$("#soap_form").submit(function(e){
		// prevent the form from submitting
		e.preventDefault();
					$("#BTNsoap_form").attr("disabled", true);
					$("#BTNsoap_form").text('Processing ...');
		$.ajax({
			url: DOMAIN+"/includes/process.php",
			type: 'POST',
			processData: false, // important 
            contentType: false, // important
			// pass the form in the FormData constructor to send all the data inside the form
			data: new FormData(this),
			success: function(result) {
				if ($.trim(result)=="ADDED_SOAP"){
					
					Swal({
					  type: 'success',
					  title: "NEW CONSULTATION SUCCESSFULLY ADDED!",
					  showConfirmButton: false,
					  timer: 1500
					}).then(function() {
					window.history.go(-1);
					});	

				}else{
					Swal({
					  type: 'error',
					  title: result,
					  showConfirmButton: true,
					  //timer: 1500
					}).then(function() {
					//window.location.reload();
					});	
				}
					$("#BTNsoap_form").attr("disabled", false);
			

			},
			error: function(xhr, result, errorThrown){
				Swal({
					  type: 'error',
					  title: result,
					  showConfirmButton: true,
					  //timer: 1500
					}).then(function() {
					//window.location.reload();
					});
					$("#BTNsoap_form").attr("disabled", false);
					$("#BTNsoap_form").text('Submit');

			}
		});
		//$('#picture').val('');
		//$('#body').val('');
	})
		
		$("#addpresciption_form").submit(function(e){
		// prevent the form from submitting
		e.preventDefault();
		$.ajax({
			url: DOMAIN+"/includes/process.php",
			type: 'POST',
			processData: false, // important 
            contentType: false, // important
			// pass the form in the FormData constructor to send all the data inside the form
			data: new FormData(this),
			success: function(result) {
				console.log(result);	
					if ($.trim(result)=="PrescriptionGenericName_ADDED"){
						Swal({
						  type: 'success',
						  title: 'PRESCRIPTION SUCCESSFULLY UPDATED',
						  showConfirmButton: false,
						  timer: 1500
						}).then(function() {
						window.location.reload();
						});
						
					}else{
						Swal({
						  type: 'error',
						  title: result,
						  showConfirmButton: true,
						  //timer: 1500
						}).then(function() {
						//window.location.reload();
						});							
					}
			},
			error: function(xhr, result, errorThrown){
				console.log(result);
					Swal({
					  type: 'error',
					  title: result,
					  showConfirmButton: true,
					  //timer: 1500
					}).then(function() {
					//window.location.reload();
					});
				}
		});
		//$('#picture').val('');
		//$('#body').val('');
	})
		$("#vitals_form").submit(function(e){
		// prevent the form from submitting
		e.preventDefault();
		$.ajax({
			url: DOMAIN+"/includes/process.php",
			type: 'POST',
			processData: false, // important 
            contentType: false, // important
			// pass the form in the FormData constructor to send all the data inside the form
			data: new FormData(this),
			success: function(result) {
				console.log(result);	
					if ($.trim(result)=="VITALS_SUCCESSFULLY_ADDED"){
						Swal({
						  type: 'success',
						  title: 'VITALS SUCCESSFULLY UPDATED',
						  showConfirmButton: false,
						  timer: 1500
						}).then(function() {
						window.location.reload();
						});
						
					}else{
						Swal({
						  type: 'error',
						  title: result,
						  showConfirmButton: true,
						  //timer: 1500
						}).then(function() {
						//window.location.reload();
						});							
					}
			},
			error: function(xhr, result, errorThrown){
				console.log(result);
					Swal({
					  type: 'error',
					  title: result,
					  showConfirmButton: true,
					  //timer: 1500
					}).then(function() {
					//window.location.reload();
					});
				}
		});
		//$('#picture').val('');
		//$('#body').val('');
	})
		
	
		$("#DOCPERSONAL_INFO").submit(function(e){
		// prevent the form from submitting
		e.preventDefault();
		$.ajax({
			url: DOMAIN+"/includes/process.php",
			type: 'POST',
			processData: false, // important 
            contentType: false, // important
			// pass the form in the FormData constructor to send all the data inside the form
			data: new FormData(this),
			success: function(result) {
				console.log(result);
					if ($.trim(result)=="UpdateDocPersonalInfo_Success"){
						Swal({
						  type: 'success',
						  title: 'SUCCESSFULLY UPDATED',
						  showConfirmButton: false,
						  timer: 1500
						}).then(function() {
						window.location.reload();
						});
						
					}
			},
			error: function(xhr, result, errorThrown){
				console.log(result);
					Swal({
					  type: 'error',
					  title: result,
					  showConfirmButton: true,
					  //timer: 1500
					}).then(function() {
					//window.location.reload();
					});
				}
		});
		//$('#picture').val('');
		//$('#body').val('');
	})
		
	
			$("#LICENSE_TRAINING").submit(function(e){
		// prevent the form from submitting
		e.preventDefault();
		$.ajax({
			url: DOMAIN+"/includes/process.php",
			type: 'POST',
			processData: false, // important 
            contentType: false, // important
			// pass the form in the FormData constructor to send all the data inside the form
			data: new FormData(this),
			success: function(result) {
				console.log(result);
					if ($.trim(result)=="UpdateLicenseEducation_SUCCESS"){
						Swal({
						  type: 'success',
						  title: 'SUCCESSFULLY UPDATED',
						  showConfirmButton: false,
						  timer: 1500
						}).then(function() {
						window.location.reload();
						});
						
					}
				},
			error: function(xhr, result, errorThrown){
				console.log(result);
					Swal({
					  type: 'error',
					  title: result,
					  showConfirmButton: true,
					  //timer: 1500
					}).then(function() {
					//window.location.reload();
					});
			}
		});
		//$('#picture').val('');
		//$('#body').val('');
	})
		
			$("#PATIENTUSERNAME_INFO").submit(function(e){
		// prevent the form from submitting
		e.preventDefault();
		$.ajax({
			url: DOMAIN+"/includes/process.php",
			type: 'POST',
			processData: false, // important 
            contentType: false, // important
			// pass the form in the FormData constructor to send all the data inside the form
			data: new FormData(this),
			success: function(result) {
				alert(result);
				window.location.reload();
			},
			error: function(xhr, result, errorThrown){
				alert('Request failed.');
			}
		});
		//$('#picture').val('');
		//$('#body').val('');
	})
			$("#PATIENTPASSWORD_INFO").submit(function(e){
		// prevent the form from submitting
		e.preventDefault();
		$.ajax({
			url: DOMAIN+"/includes/process.php",
			type: 'POST',
			processData: false, // important 
            contentType: false, // important
			// pass the form in the FormData constructor to send all the data inside the form
			data: new FormData(this),
			success: function(result) {
				alert(result);
				window.location.reload();
			},
			error: function(xhr, result, errorThrown){
				alert('Request failed.');
			}
		});
		//$('#picture').val('');
		//$('#body').val('');
	})
		
			$("#PATIENTPERSONAL_INFO").submit(function(e){
		// prevent the form from submitting
		e.preventDefault();
		$.ajax({
			url: DOMAIN+"/includes/process.php",
			type: 'POST',
			processData: false, // important 
            contentType: false, // important
			// pass the form in the FormData constructor to send all the data inside the form
			data: new FormData(this),
			success: function(result) {
				alert(result);
				window.location.reload();
			},
			error: function(xhr, result, errorThrown){
				alert('Request failed.');
			}
		});
		//$('#picture').val('');
		//$('#body').val('');
	})
		
			$("#hips_sms").submit(function(e){
		// prevent the form from submitting
		e.preventDefault();
		$.ajax({
			url: DOMAIN+"/includes/sms.php",
			type: 'POST',
			processData: false, // important 
            contentType: false, // important
			// pass the form in the FormData constructor to send all the data inside the form
			data: new FormData(this),
			success: function(result) {
				alert(result);
				window.location.reload();
			},
			error: function(xhr, result, errorThrown){
				alert('Request failed.');
			}
		});
		//$('#picture').val('');
		//$('#body').val('');
	})
			$("#forgot_form").submit(function(e){
		// prevent the form from submitting
		e.preventDefault();
		$.ajax({
			url: DOMAIN+"/includes/process.php",
			type: 'POST',
			processData: false, // important 
            contentType: false, // important
			// pass the form in the FormData constructor to send all the data inside the form
			data: new FormData(this),
			success: function(result) {
				if ($.trim(result)=="ERROR_CODE"){
					
					alert("Verification Code Error.");
					
				}else if ($.trim(result)=="PASSWORD_NOT_MATCH"){
				alert("Password didn't matched. Try Again");
				}else if ($.trim(result)=="STRLEN"){
					alert("Please enter more than 9 digit password.");
				}else if ($.trim(result)=="SUCCESS"){
				alert("Successfully");
				window.location.href = "login.php";

				}else{
					alert(result);
				alert("ERROR OCCURED! Please Contact System Administrator.");
				}
			},
			error: function(xhr, result, errorThrown){
				alert('Request failed.');
			}
		});
		//$('#picture').val('');
		//$('#body').val('');
	})
		
		
			$("#AddNewPatient").submit(function(e){
		// prevent the form from submitting
		e.preventDefault();
		$.ajax({
			url: DOMAIN+"/includes/process.php",
			type: 'POST',
			processData: false, // important 
            contentType: false, // important
			// pass the form in the FormData constructor to send all the data inside the form
			data: new FormData(this),
			success: function(result) {
				//alert(result);
				if ($.trim(result)=="EMAIL_ALREADY_EXISTS"){
					Swal({
					  type: 'warning',
					  title: 'EMAIL ALREADY EXIST!.',
					  showConfirmButton: true,
					  //timer: 1500
					}).then(function() {
					//window.location.reload();
					});	
				}else{
					//alert("Successfully Added!");
					Swal({
					  type: 'success',
					  title: 'PATIENT SUCCESSFULLY ADDED!',
					  showConfirmButton: false,
					  timer: 1500
					}).then(function() {
										window.location.href = "?p=patientDetails&id=last";
					});

					
				}
			},
			error: function(xhr, result, errorThrown){
					console.log(result);
					
					Swal({
					  type: 'error',
					  title: result,
					  showConfirmButton: true,
					  //timer: 1500
					}).then(function() {
					//window.location.reload();
					});
//				alert('Request failed.');
			}
		});
		//$('#picture').val('');
		//$('#body').val('');
	})
		
		
		$("#addnewclinic_form").submit(function(e){
		// prevent the form from submitting
		e.preventDefault();
		$.ajax({
			url: DOMAIN+"/includes/process.php",
			type: 'POST',
			processData: false, // important 
            contentType: false, // important
			// pass the form in the FormData constructor to send all the data inside the form
			data: new FormData(this),
			success: function(result) {
				//alert(result);
				if ($.trim(result)=="CLINIC_ADDED"){
					Swal({
					  type: 'success',
					  title: 'Clinic successfully added',
					  showConfirmButton: false,
					  timer: 1500
					}).then(function() {
					window.location.reload();
					});
				}else if ($.trim(result)=="CLINIC_NAME_EXIST"){
					Swal({
					  type: 'warning',
					  title: 'Clinic name already exist!',
					  showConfirmButton: true,
					  //timer: 1500
					}).then(function() {
					//window.location.reload();
					});
				}else{
					
					Swal({
					  type: 'error',
					  title: result,
					  showConfirmButton: true,
					  //timer: 1500
					}).then(function() {
					//window.location.reload();
					});
					
				}
			},
			error: function(xhr, result, errorThrown){
				alert('Request failed.');
			}
		});
		//$('#picture').val('');
		//$('#body').val('');
	})
		$("#updateclinic_form").submit(function(e){
		// prevent the form from submitting
		e.preventDefault();
		$.ajax({
			url: DOMAIN+"/includes/process.php",
			type: 'POST',
			processData: false, // important 
            contentType: false, // important
			// pass the form in the FormData constructor to send all the data inside the form
			data: new FormData(this),
			success: function(result) {
				//alert(result);
				if ($.trim(result)=="CLINIC_SUCCESS"){
					Swal({
					  type: 'success',
					  title: 'CLINIC SUCCESSFULLY UPDATED',
					  showConfirmButton: false,
					  timer: 1500
					}).then(function() {
					window.location.href = "?p=home";
					});
					
				}else if ($.trim(result)=="CLINIC_NAME_EXIST"){
			
					Swal({
					  type: 'warning',
					  title: 'CLINIC NAME ALREADY EXIST!.',
					  showConfirmButton: true,
					  //timer: 1500
					}).then(function() {
					//window.location.href = "?p=home";
					});

				}else{
					console.log(result);
					
					Swal({
					  type: 'error',
					  title: result,
					  showConfirmButton: true,
					  //timer: 1500
					}).then(function() {
					//window.location.reload();
					});
					
				}
			},
			error: function(xhr, result, errorThrown){
					Swal({
					  type: 'error',
					  title: result,
					  showConfirmButton: true,
					  //timer: 1500
					}).then(function() {
					//window.location.reload();
					});
			}
		});
		//$('#picture').val('');
		//$('#body').val('');
	})
	
			$("#EditPatient").submit(function(e){
		// prevent the form from submitting
		e.preventDefault();
		$("#BTNsubmit").attr("disabled", true);
		$.ajax({
			url: DOMAIN+"/includes/process.php",
			type: 'POST',
			processData: false, // important 
            contentType: false, // important
			// pass the form in the FormData constructor to send all the data inside the form
			data: new FormData(this),
			success: function(result) {
				
				if ($.trim(result)=="UPDPATIENTINFO_SUCCESS"){
					Swal({
					  type: 'success',
					  title: 'Patient Profile successfully Updated!',
					  showConfirmButton: false,
					  timer: 1500
					}).then(function() {
					window.location.reload();
					});
					
					//window.location.reload();
				}else{
					console.log(result);
					
					Swal({
					  type: 'error',
					  title: result,
					  showConfirmButton: true,
					  //timer: 1500
					}).then(function() {
					//window.location.reload();
					});
						
				}
					$("#BTNsubmit").attr("disabled", false);
	
			},
			error: function(xhr, result, errorThrown){
				console.log(result);
				
					Swal({
					  type: 'error',
					  title: "Request failed!",
					  showConfirmButton: true,
					  //timer: 1500
					}).then(function() {
					//window.location.reload();
					});
		
		$("#BTNsubmit").attr("disabled", f);

			}
		});
		//$('#picture').val('');
		//$('#body').val('');
	})
		
	
		
$('.send_button').click(function(){

    var data_id = $(this).attr("data-id");
    var data_status = $(this).attr("data-idd");
 if (!confirm('Are you sure?')) return false;
    $.ajax
    ({ 
        url: '/includes/sms.php',
        data: {"app_CID": data_id, "app_status": data_status},
        //data: {"app_status": data_status},
        type: 'POST',
			success: function(result) {
				alert(result);
				/* if (result=="SUCCESSFULLY_ADDED"){
					alert("SUCCESSFULLY_ADDED");						
					window.location.reload();
				}else{
					alert("ERROR OCCURED!");
					
				} */
			},
			error: function(xhr, result, errorThrown){
				alert('Request failed.');
			} 
		   
		   
			});


});
	
	
 $('#modalContactForm').on('click', '.btn-info', function(e){
     var vfname = $('#fname').val();
	 var vemail = $('#email').val();
   
	
			$.post("miscellaneous/result.php", //Required URL of the page on server
               { // Data Sending With Request To Server
                  fname:vfname,
				  email:vemail,
               },
			function(response,status){ // Required Callback Function
             $("#result").html(response);//"response" receives - whatever written in echo of above PHP script.
            
          });
		  
     $('#s').modal('hide');
   });
   
	
	$("#modalContactForm").submit(function(e){
		// prevent the form from submitting
		e.preventDefault();
		//$("#BTNsubmit").attr("disabled", true);
		$.ajax({
			url: DOMAIN+"/miscellaneous/result.php",
			type: 'POST',
			processData: false, // important 
            contentType: false, // important
			// pass the form in the FormData constructor to send all the data inside the form
			data: new FormData(this),
			success: function(response,status) {
				//if ($.trim(result)=="UPDPATIENTINFO_SUCCESS"){
					Swal({
					  type: 'success',
					  title: 'Patient Profile successfully Updated!',
					  showConfirmButton: false,
					  timer: 1500
					}).then(function() {
					window.location.reload();
					});
					
					//window.location.reload();
				//}
				 $("#result").html(response);
					//$("#BTNsubmit").attr("disabled", false);
	  $('#s').modal('hide');
			},
			error: function(xhr, result, errorThrown){
				console.log(result);
				
					Swal({
					  type: 'error',
					  title: "Request failed!",
					  showConfirmButton: true,
					  //timer: 1500
					}).then(function() {
					//window.location.reload();
					});
		
		//$("#BTNsubmit").attr("disabled", f);

			}
		});
		//$('#picture').val('');
		//$('#body').val('');
	})
	
			
$('.tab1').click(function(){
var data_status = "tab1";
localStorage.setItem('PatientDetailsactiveTab', data_status);
var PatientDetailsactiveTab = localStorage.getItem('PatientDetailsactiveTab');
 	console.log(PatientDetailsactiveTab);
		 		
	} )	
$('.tab2').click(function(){
var data_status = "tab2";
localStorage.setItem('PatientDetailsactiveTab', data_status);
var PatientDetailsactiveTab = localStorage.getItem('PatientDetailsactiveTab');
 	console.log(PatientDetailsactiveTab);
		 		
	} )	
$('.tab3').click(function(){
var data_status = "tab3";
localStorage.setItem('PatientDetailsactiveTab', data_status);
var PatientDetailsactiveTab = localStorage.getItem('PatientDetailsactiveTab');
 	console.log(PatientDetailsactiveTab);
		 		
	} )	
	
	
$('.delete_clinic').click(function(){

    var data_id = $(this).attr("data-id");
    var data_status = $(this).attr("data-idd");
	

Swal({
  title: 'Are you sure?',
  text: "You won't be able to revert this!",
  type: 'warning',
  showCancelButton: true,
  confirmButtonColor: '#3085d6',
  cancelButtonColor: '#d33',
  confirmButtonText: 'Yes, delete it!'
}).then((result) => {
  if (result.value) {
	  
 $.ajax
    ({ 
        url: '/includes/process.php',
        data: {"clinic_CID": data_id, "clinic_status": data_status},
        //data: {"app_status": data_status},
        type: 'POST',
		success: function(result) {
			
					console.log(result);
					Swal(
					  'Deleted!',
					  'Your Clinic has been deleted.',
					  'success'
					).then(function() {
					window.location.reload();
					});							
	
	
					},
					error: function(xhr, result, errorThrown){
					
					console.log(result);
					
					Swal({
					  type: 'error',
					  title: result,
					  showConfirmButton: true,
					  //timer: 1500
					}).then(function() {
					//window.location.reload();
					});
					
					}   
		   
		   
	})	  
	  
	  

  }
})















});

	

	
	
	
	
	
	
	
	
	
	
	
	
	

})

					function ShowByDoctor() {
						doctor = document.getElementById('doctor');	
						specialization = document.getElementById('specialization');	
						Mylocation = document.getElementById('location');	
						date = document.getElementById('date');	
						
						doctor = doctor.value;				
						specialization = specialization.value;								
						Mylocation = Mylocation.value;								
						date = date.value;			
						
						if (doctor == "") {
							document.getElementById("txtHint").innerHTML = "No data to be shown";
							return;
						} else {
						if (window.XMLHttpRequest) {
						// code for IE7+, Firefox, Chrome, Opera, Safari
						xmlhttp = new XMLHttpRequest();
						} else {
						// code for IE6, IE5
						xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
						}
						xmlhttp.onreadystatechange = function() {
						if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
						document.getElementById("txtHint").innerHTML = xmlhttp.responseText;
						}
						};
						xmlhttp.open("GET","getschedule.php?doctor="+doctor+"&specialization="+specialization+"&location="+Mylocation+"&date="+date,true);
						console.log(doctor);
						console.error();
						xmlhttp.send();
						}
						}	
	