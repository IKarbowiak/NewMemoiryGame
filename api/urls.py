from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from api.game.views import CardList, GameViewSet
from api.themes.views import ThemesView

urlpatterns = {
    url(r'^decks/$', CardList.as_view(), name='create'),
    url(r'^themes/$', ThemesView.as_view(), name='themes'),
    url(r'^game/$', GameViewSet.as_view({'post': 'create', 'get': 'list'}), name='game'),
    # url(r'scores/$', GameViewSet.as_view(), name='scores')
}

urlpatterns = format_suffix_patterns(urlpatterns)
