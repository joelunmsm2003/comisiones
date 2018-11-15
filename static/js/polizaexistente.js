var app = angular.module('myApp', []);

app.config(function($interpolateProvider){
    $interpolateProvider.startSymbol('{[{').endSymbol('}]}');
    });
app.controller('myCtrl', function($scope,$http,$filter) {


$scope.nav=true




$('#buscapolizaexistente').modal('show')





$http.get("/polizas").success(function(response) {


            $scope.polizas = response;

            $(".container").css("display", "block");



        });





    $scope.ingresar = function(data){

    	console.log(data)



        window.location="/menu/"

    }


    $scope.poliza = function(data){

    	console.log(data)


		$('#myModal').modal('show')

    }

    $scope.polizaexistente=function(data){

		$('#buscapolizaexistente').modal('show')
		$('#myModal').modal('hide')


		


    }

    $scope.guardarpoliza=function(){




    swal({
     title: "Capital Financial Partners",
     text: "Datos de poliza guardado",
     type: "success",
     showConfirmButton: false,
     timer: 3000
     })


    setTimeout(function(){ window.location="/dashboard/"; }, 3000);
    }

    $scope.irapoliza=function(data){



    	$scope.datosdepoliza = $filter('filter')($scope.polizas,data)[0];

    	console.log('$scope.datosdepoliza',$scope.datosdepoliza)

    	$('#buscapolizaexistente').modal('hide')



    }

    $scope.polizanueva=function(data){

		$('#cliente').modal('show')
		$('#myModal').modal('hide')
    }

    $scope.nuevocliente=function(data){


    	

    	
    	$('#propuestacliente').modal('hide')

		$('#datoscliente').modal('show')

		$('#cliente').modal('hide')

    }

     $scope.asignaagente=function(data){

    	
  		$scope.agentedato =data

		$('#agente').modal('hide')

    }

    $scope.clienteexistente=function(data){

    }

    $scope.datosdepoliza={}

    $scope.propuestacliente=function(data){

    	

    	$scope.datosdepoliza.cliente=data

    	console.log($scope.datosdepoliza)


		$('#propuestacliente').modal('show')

		$('#datoscliente').modal('hide')
    }

     $scope.agente=function(data){

    	console.log(data)


		$('#agente').modal('show')

		$('#datoscliente').modal('hide')

		$('#propuestacliente').modal('hide')

		$http.get("/agentes").success(function(response) {

			$scope.agentes = response;
	       
	    });
    }




})
