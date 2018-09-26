(function(){
    angular.module('memo')
        .controller('scoreCtrl', ['$scope', '$http', function($scope, $http){
            $scope.scores = {}
            getApi = false
            $http.get('api/themes').then(function(response){
                console.log(response.data)
                $scope.themes = response.data.themes
                themes = response.data.themes
                $http.get('/api/game/').then(function(response){
                    console.log(themes)
                    console.log(response.data)
                    games = response.data;
                    for (let theme of themes){
                        for (let size of ['10', '16', '20']) {
                            $scope.scores[theme+size] = []
                        }
                    }

                    for (let game of games){
                        $scope.scores[game.game_theme + game.cards_number].push(game)
                    }
                    getApi = true
                })

            })

        }])
})();