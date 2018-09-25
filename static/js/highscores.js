(function(){
    angular.module('memo')
        .controller('scoreCtrl', ['$scope', '$http', function($scope, $http){
            $http.get('api/themes').then(function(response){
                console.log(response.data)
                $scope.themes = response.data.themes

            })
            $http.get('/api/game/').then(function(response){
                console.log(response.data)


            })

        }])
})();