(function(){
    api_url = '/api/decks/';

    angular.module('flip')
        .controller('flipCtrl', ['$scope', '$http', function($scope, $http){
            $http.get('api/decks').then(function(response){
                $scope.cards = [];
                let row = [];
                let data_with_cards = [].concat(response.data, response.data);
                data_with_cards.sort(function() {
                    return .5 - Math.random();
                });
                for (let card of data_with_cards) {
                    row.push(card)
                    if (row.length == 4){
                        $scope.cards.push(row)
                        row = []
                    }
                    console.log(row)
                }
                console.log($scope.cards)
            }
        )}])

})()