(function(){

    angular.module('memo')
        .controller('themeCtrl', ['$scope', '$http', '$interval', function($scope, $http, $interval){

            $http.get('api/themes').then(function(response){
                console.log(response.data)
                $scope.themes = response.data.themes

            })
//
//            $scope.themes = ['Dogs', 'Cats', 'Wild Animals']
//            $scope.choose_theme = theme => {
//                console.log(theme)
//
//            }



    }])
})();