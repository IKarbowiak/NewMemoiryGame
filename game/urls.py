from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.conf.urls import url


urlpatterns = [
    path('', views.start_site, name='start_site'),
    url(r'^game/?', TemplateView.as_view(template_name='game/game.html'))
    # path('dogs/', views.dogs_deck, name='dogs_deck'),
]

