var app = angular.module('myApp', []);

app.config(function($interpolateProvider){
    $interpolateProvider.startSymbol('{[{').endSymbol('}]}');
    });
app.controller('myCtrl', function($scope,$http,$filter) {


   $scope.nav=true


    $scope.oculto=1


    $scope.grande=false


    $('#cliente').modal('show')


    $http.get("/listaramos_1").success(function(response) { 

        $scope.ramos = response; 

    });


    $http.get("/clientes").success(function(response) { 

        $scope.clientes = response; 

    });

     $scope.buscacompania=function(data){

        console.log(data)


        $http.get("/listacia_1/"+data.id).success(function(response) { 

        $scope.cias = response; 

    });


    }

    $scope.buscaproducto=function(data){

        console.log(data)


        $http.get("/listaproductos/"+data.compania).success(function(response) { 

        $scope.productos = response; 

    });


    }

    $scope.asignaproducto=function(data){

        console.log(data)


       $scope.producto=data


    }


    $scope.entramenu=function(){


        console.log('hshshshshs')

        $scope.oculto=0


    }

    $(".edit").css("display", "none");

    $scope.editar=function(){

        console.log('editando...')

        $(".edit").css("display", "block");
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

    


    $scope.ingresar = function(data){

    	console.log(data)

        window.location="/menu/"

    }


    $scope.poliza = function(data){

    	console.log(data)


		$('#myModal').modal('show')

    }


    $scope.asignacliente = function(data){

        $scope.cliente=data



    }

    $scope.polizaexistente=function(data){

		$('#buscapolizaexistente').modal('show')
		$('#myModal').modal('hide')


		$http.get("/polizas").success(function(response) {


			$scope.polizas = response;

			$scope.search=''

	       
	    });







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

    $scope.clienteexistente=function(data){



    	$('#propuestacliente').modal('hide')

		$('#datoscliente').modal('show')

		$('#cliente').modal('hide')

    }

    $scope.clientenuevo=function(data){




        $('#nuevocliente').modal('show')


    }




     $scope.asignaagente=function(data){

    	
  		$scope.agentedato =data


        console.log($scope.agentedato)

		$('#agente').modal('hide')

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



        $(".container").css("display", "block");

})
