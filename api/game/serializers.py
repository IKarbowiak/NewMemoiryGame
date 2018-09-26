from rest_framework import serializers
from game.models import MemoCard, Game


class CardDeckSerializer(serializers.ModelSerializer):
    """ Serializer to map the Model instance into JSON format """

    class Meta:
        model = MemoCard
        fields = ('id', 'name', 'path', 'theme')


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('player', 'date', 'cards_number', 'time', 'guesses', 'game_theme')
