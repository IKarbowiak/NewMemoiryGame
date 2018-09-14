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
                let count = 0;
                for (let card of data_with_cards) {
                    let new_card = {'id': count, 'path': card.path, 'name': card.name}
                    row.push(new_card)
                    if (row.length == 5){
                        $scope.cards.push(row)
                        row = []
                    }
                    count ++;
                }
            })

            let flipped_cards = []
            $scope.guesses = 0
            $scope.flipCard = card => {
                if (!card.isFlipped && flipped_cards.length < 2){
                    card.isFlipped =! card.isFlipped;
                    flipped_cards.push(card)
                    if (flipped_cards.length === 2){
                        $scope.guesses ++
                        if (flipped_cards[0].name === flipped_cards[1].name) {
                            flipped_cards = []
                        }
                        else {
//                            sleep(2000)
                            setTimeout(_ => {
                            flipped_cards[0].isFlipped = false;
                            flipped_cards[1].isFlipped = false;
                            flipped_cards = [];
                            $scope.$apply();
                            }, 1000)
                        }
                    }
                }

                console.log($scope.cards)
            }
//            function sleep(milliseconds) {
//                var start = new Date().getTime();
//                for (var i = 0; i < 1e7; i++) {
//                    if ((new Date().getTime() - start) > milliseconds){
//                        break;
//                }
//              }
//            }
        }])

})()

