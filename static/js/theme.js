(function(){

    angular.module('memo')
        .controller('themeCtrl', ['$scope', '$http', '$interval', function($scope, $http, $interval){

            $http.get('/api/themes/').then(function(response){
                console.log(response.data)
                $scope.themes = response.data.themes
            })
    }])
})();