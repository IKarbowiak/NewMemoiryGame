from rest_framework import viewsets, views
from game.models import Deck
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
import random


class ThemesView(views.APIView):

    render_classes = (JSONRenderer, )

    def get(self, request, format=None):
        themes = Deck.objects.all().values_list('theme', flat=True).distinct()
        content = {'themes': themes}
        return Response(content)

# class ThemesViewSet(viewsets.ViewSet):
#
#     queryset = Deck.objects.all().values_list('theme', flat=True).distinct()
#     serializer_class = ThemesSerializer
#
#     def list(self, request):
#         serializer = ThemesSerializer
#     # def perform_create(self, serializer):
#     #     """ Save the post data when creating a new memocard. """
#     #     serializer.save()
