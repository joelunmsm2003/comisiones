var app = angular.module('myApp', []);

app.config(function($interpolateProvider){
    $interpolateProvider.startSymbol('{[{').endSymbol('}]}');
    });
app.controller('myCtrl', function($scope,$http,$filter) {


$scope.nav=false







    $scope.ingresar = function(data){

    	console.log(data)



        window.location="/dashboard/"

    }


    $scope.poliza = function(data){

    	console.log(data)


		//$('#myModal').modal('show')

        window.location="/admin/app/poliza"
    }   

    $scope.polizaexistente=function(data){

		$('#buscapolizaexistente').modal('show')
		$('#myModal').modal('hide')


		$http.get("/polizas").success(function(response) {


			$scope.polizas = response;

			$scope.search=''

	       
	    });


    }

    $scope.entramenu=function(){


        console.log('hshshshshs')


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
