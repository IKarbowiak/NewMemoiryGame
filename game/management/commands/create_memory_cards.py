from game.models import MemoCard
from django.core.management.base import BaseCommand
import os


class Command(BaseCommand):

    def handle(self, *args, **options):
        for filename in os.listdir("C:\\Users\\karbowia\\Documents\\MemoryGame\\memorygame\\pictures"):
            if filename.endswith(".jpg"):
                print("Card name: " + filename)
                card, create = MemoCard.objects.get_or_create(name=filename.rstrip(".jpg"), path="../../static/src/"+filename, theme="Dogs")
                if create:
                    print("Create")
                else:
                    card.path="../../static/src/"+filename
                    print("Update")
                # card.theme = 'Dogs'
                card.save()



