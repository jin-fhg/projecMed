$(document).ready(function(){
    $.ajax({
        url: './php/ajaxfile.php',
        type: 'get',
        dataType: 'JSON',
        success: function(response){
            var len = response.length;
            for(var i=0; i<len; i++){

				//Parse Doctor Info
				$(".name").html(response[i].name);				
				$(".email").html(response[i].email);				
				$(".email").attr('title', response[i].email);
				$(".email").attr('title', response[i].email);

				$(".intro").html(response[i].intro);				
				$(".education").html(response[i].education);				
				$(".doctor_address").html(response[i].emp_address);		
				
				$(".affiliation").html(response[i].affiliation);				
				
				
				$(".doctor_dp").attr('src', response[i].dp);				
				$(".doctor_dp").attr('title', response[i].name);
				
            }

        }
    });
   
});