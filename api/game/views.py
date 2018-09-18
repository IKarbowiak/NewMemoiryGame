from rest_framework import generics
from .serializers import CardDeckSerializer
from game.models import Deck, MemoCard
import random


class CardList(generics.ListCreateAPIView):
    """ This class defines the create behavior of our rest api. """
    # decks = Deck.objects.filter(theme='Dogs')
    # queryset = random.sample(list(decks), 1)[0].cards
    serializer_class = CardDeckSerializer

    def get_queryset(self):
        # queryset = Deck.objects.order_by('?').all()     # random order
        queryset = MemoCard.objects.all().order_by('?')

        theme = self.request.query_params.get('theme', '')
        size = self.request.query_params.get('size', '10')

        if theme:
            queryset = queryset.filter(theme=theme)

        return queryset[:int(size)]

    def perform_create(self, serializer):
        """ Save the post data when creating a new memocard. """
        serializer.save()


