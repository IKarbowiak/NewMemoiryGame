from django.urls import path
from django.conf.urls import url
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path('', views.start_site, name='start_site'),
    url(r'^game/?', TemplateView.as_view(template_name='game/game.html')),
    url(r'^high_scores/?', TemplateView.as_view(template_name='game/high_scores.html'))
    # url(r'^dogs/?', TemplateView.as_view(template_name='../templates/game/game.html'))
    # path('dogs/', views.dogs_deck, name='dogs_deck'),
]

