from django.shortcuts import render
from .models import Deck
import random


def start_site(request):
    themes = Deck.objects.all().values_list('theme', flat=True).distinct()
    return render(request, 'game/start_site.html', {'themes': themes})

#
# def dogs_deck(request):
#     decks = Deck.objects.filter(theme='Dogs').exclude(cards=None)
#     deck = random.sample(list(decks), 1)[0]
#     deck_cards = deck.cards.all()
#     cards = list(deck_cards)
#     cards.extend(deck_cards)
#     random.shuffle(cards)
#     cards_in_row = [[card for card in cards[i:i+4]] for i in range(0, len(cards), 4)]
#
#     return render(request, 'game/dogs_deck.html', {'cards': cards_in_row})

