from rest_framework import generics
from .serializers import CardDeckSerializer
from game.models import Deck, MemoCard
import random


class DeckList(generics.ListCreateAPIView):
    """ This class defines the create behavior of our rest api. """
    decks = Deck.objects.filter(theme='Dogs')
    queryset = random.sample(list(decks), 1)[0].cards
    # queryset = cards | cards
    # random.seed()
    # cards = list(deck_cards)
    # cards.extend(deck_cards)
    # random.shuffle(cards)
    # cards = [card.name for card in cards]
    # # cards_in_row = [[card for card in cards[i:i+4]] for i in range(0, len(cards), 4)]
    # queryset = MemoCard.objects.filter(name__in=cards)
    serializer_class = CardDeckSerializer

    def perform_create(self, serializer):
        """ Save the post data when creating a new memocard. """
        serializer.save()


