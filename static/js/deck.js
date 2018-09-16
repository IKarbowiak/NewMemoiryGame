(function(){
    api_url = '/api/decks/';

    angular.module('flip')
        .controller('flipCtrl', ['$scope', '$http', '$interval', '$uibModal', function($scope, $http, $interval, $uibModal){
            $http.get('api/decks').then(function(response){
                $scope.cards = [];
                let row = [];
                let data_with_cards = [].concat(response.data, response.data);
                data_with_cards.sort(function() {
                    return .5 - Math.random();
                });
                let count = 0;
                for (let card of data_with_cards) {
                    let new_card = {'id': count, 'path': card.path, 'name': card.name, 'isFlipped': false};
                    row.push(new_card);
                    if (row.length === 5){
                        $scope.cards.push(row);
                        row = []
                    }
                    count ++;
                }
            });

            let start_game = false;
            let flipped_cards = [];
            $scope.guesses = 0;
            $scope.time = 0;
            $scope.end = false;
            $scope.flipCard = card => {
                if (!card.isFlipped && flipped_cards.length < 2){
                    // open_modal();
                    if (!start_game) {
                        console.log("HERE");
                        start_game = true;
                        timer = $interval(function () {
                            $scope.time += 1000;
                        }, 1000)
                    }

                    card.isFlipped =! card.isFlipped;
                    flipped_cards.push(card);
                    if (flipped_cards.length === 2){
                        $scope.guesses ++;
                        if (flipped_cards[0].name === flipped_cards[1].name) {
                            flipped_cards = []
                        }
                        else {
                            setTimeout(_ => {
                            flipped_cards[0].isFlipped = false;
                            flipped_cards[1].isFlipped = false;
                            flipped_cards = [];
                            $scope.$apply();
                            }, 1000)
                        }

                        check_for_end();
                    }
                }

                // console.log($scope.cards)
            }

            check_for_end = function () {
                let deck_cards = $scope.cards.flat();
                console.log(deck_cards);
                if (!(deck_cards.some(check))) {
                    $scope.end = true;
                    stop_game();
                    console.log("Game finished with time: ", $scope.time);
                    // open_modal()
                }
            };

            // open_modal = function () {
            //     let modalInstance = $uibModal.open({
            //         ariaLabelledBy: 'modal-title',
            //         ariaDescribedBy: 'modal-body',
            //         templateUrl: 'modalWindow.html',
            //         controller: 'ModalHandlerController',
            //         controllerAs: '$ctrl',
            //         size: 'lg',
            //         resolve: {
            //
            //         }
            //     })
            // };


            check = function(deck_card){
                console.log("Check")
                console.log(deck_card.isFlipped);
                return deck_card.isFlipped === false;
            };

            stop_game = function(){
                if (angular.isDefined(timer)){
                    $interval.cancel(timer);
                    timer = undefined;
                }
            }

        // TODO wykrywanie kiedy ktoś wygrał
        // TODO zatrzymywanie interval -- $interval.cancel(timer);


        }])

})();


angular.module('flip').controller("ModalHandlerController", function ($scope, $uibModalInstance) {

    $scope.ok = function () {
        $uibModalInstance.close('OK')
    }

});

