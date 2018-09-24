from rest_framework import generics
from .serializers import CardDeckSerializer
from game.models import MemoCard, Game
from rest_framework import viewsets
from rest_framework.response import Response
import random


class CardList(generics.ListCreateAPIView):
    """ This class defines the create behavior of our rest api. """
    # decks = Deck.objects.filter(theme='Dogs')
    # queryset = random.sample(list(decks), 1)[0].cards
    serializer_class = CardDeckSerializer

    def get_queryset(self):
        queryset = MemoCard.objects.all().order_by('?')     # random order

        theme = self.request.query_params.get('theme', '')
        size = self.request.query_params.get('size', '10')

        if theme:
            queryset = queryset.filter(theme=theme)

        return queryset[:int(size)]

    def perform_create(self, serializer):
        """ Save the post data when creating a new memocard. """
        serializer.save()


class GameViewSet(viewsets.ModelViewSet):

    def create(self, request):
        print("Game request: " + request.data)
        try:
            Game.objects.create(player=request.data['name'], date=request.data['date'], time=request.data['time'],
                                guesses=request.data['score'])

            return Response(status=201)

        except Exception as e:
            print(e)
            return Response(status=400)

