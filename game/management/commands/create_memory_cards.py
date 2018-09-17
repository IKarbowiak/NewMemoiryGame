from game.models import MemoCard
from django.core.management.base import BaseCommand
import os


class Command(BaseCommand):

    def handle(self, *args, **options):
        # for filename in os.listdir("C:\\Users\\karbowia\\Documents\\MemoryGame\\memorygame\\static\\src\\dog_breeds\\"):
        for filename in os.listdir("D:\\Programowanie\\MemoryGame\\MemoryGame_git\\static\\src\\dog_breeds"):
            if filename.endswith(".jpg"):
                print("Card name: " + filename)
                card, create = MemoCard.objects.get_or_create(name__iexact=filename.rstrip(".jpg"), theme="Dogs")
                if create:
                    print("Create")
                # else:
                #     card.path="../../static/src/"+filename
                #     print("Update")
                # card.theme = 'Dogs'

                name = filename.rstrip('.jpg')
                if '_' in filename:
                    name = name.replace('_', ' ')
                card.path = "../../static/src/dog_breeds/" + filename
                card.name = name

                card.save()



