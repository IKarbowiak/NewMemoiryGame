from rest_framework import generics
from .serializers import CardDeckSerializer
from game.models import Deck


class DeckList(generics.ListCreateAPIView):
    """ This class defines the create behavior of our rest api. """
    queryset = Deck.objects.filter(theme='Dogs')[0].cards
    serializer_class = CardDeckSerializer

    def perform_create(self, serializer):
        """ Save the post data when creating a new memocard. """
        serializer.save()


