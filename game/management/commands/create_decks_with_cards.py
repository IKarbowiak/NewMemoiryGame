from game.models import MemoCard, Deck
from django.core.management.base import BaseCommand
import random


class Command(BaseCommand):

    def handle(self, *args, **options):
        random.seed()
        cards = MemoCard.objects.filter(theme='Dogs')
        size = 10
        decks = Deck.objects.filter(theme='Dogs')
        for deck in decks:
            deck.cards.clear()
            print("Add to existing Deck")
            shuffle_cards = random.sample(list(cards), 10)
            print(shuffle_cards)
            random.shuffle(shuffle_cards)
            for card in shuffle_cards:
                deck.cards.add(card)
            deck.save()

        for i in range(5 - decks.count()):
            shuffle_cards = random.sample(list(cards), 10)
            deck = Deck.objects.create(theme='Dogs', size=size)
            for card in shuffle_cards:
                deck.cards.add(card)
            deck.save()
            print("Create new Deck")







