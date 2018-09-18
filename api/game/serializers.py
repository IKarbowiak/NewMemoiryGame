from rest_framework import serializers
from game.models import Deck, MemoCard


class CardDeckSerializer(serializers.ModelSerializer):
    """ Serializer to map the Model instance into JSON format """

    class Meta:
        model = MemoCard
        fields = ('id', 'name', 'path', 'theme')



