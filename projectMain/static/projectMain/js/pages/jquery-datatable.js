			$(document).ready(function() {
				
			$('#CLINIC').DataTable({
					"language": {                
					"infoFiltered": "",
					"emptyTable": "NO RECORDS FOUND."
					},responsive: {
					details: {
					    renderer: function ( api, rowIdx ) {
						var data = api.cells( rowIdx, ':hidden' ).eq(0).map( function ( cell ) {
						    var header = $( api.column( cell.column ).header() );
						    return  '<p style="color:#00A"><b>'+header.text()+' : </b><br>'+api.cell( cell ).data()+'</p>';
						} ).toArray().join('');
 
						return data ?    $('<table/>').append( data ) :    false;
					    }
					}
				    },
			   	processing: false,
				serverSide: false,
				ajax: "./php/clinic.php", // json datasource				
			});
						
			

		
			$('a[data-toggle="tab"]').on('shown.bs.tab', function (e) {
				$($.fn.dataTable.tables(true)).DataTable()
				   .columns.adjust()
				   .responsive.recalc();
			}); 				
				

			$('#PATIENT').DataTable({
					"language": {                
					"infoFiltered": "",
					"emptyTable": "NO RECORDS FOUND."
					},responsive: {
					details: {
					    renderer: function ( api, rowIdx ) {
						var data = api.cells( rowIdx, ':hidden' ).eq(0).map( function ( cell ) {
						    var header = $( api.column( cell.column ).header() );
						    return  '<p style="color:#00A"><b>'+header.text()+' : </b><br>'+api.cell( cell ).data()+'</p>';
						} ).toArray().join('');
 
						return data ?    $('<table/>').append( data ) :    false;
					    }
					}
				    },
			   	processing: false,
				serverSide: false,
				ajax: "./php/patient.php", // json datasource				
			});
						
			

		
			$('a[data-toggle="tab"]').on('shown.bs.tab', function (e) {
				$($.fn.dataTable.tables(true)).DataTable()
				   .columns.adjust()
				   .responsive.recalc();
			}); 				
				
				
				
				
				
				
				
				
				/*
				
			   var dataTable =  $('.js-basic-example').DataTable( {
			   	    responsive: {
					details: {
					    renderer: function ( api, rowIdx ) {
						var data = api.cells( rowIdx, ':hidden' ).eq(0).map( function ( cell ) {
						    var header = $( api.column( cell.column ).header() );
						    return  '<p style="color:#00A">'+header.text()+' : '+api.cell( cell ).data()+'</p>';
						} ).toArray().join('');
 
						return data ?    $('<table/>').append( data ) :    false;
					    }
					}
				    },
			   	processing: true,
				serverSide: true,
				ajax: "./php/medical-notes.php", // json datasource
			    } );*/
			} );
	