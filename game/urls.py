from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.conf.urls import url


urlpatterns = [
    path('', views.start_site, name='start_site'),
    url(r'^dogs/?', TemplateView.as_view(template_name='game/dogs_deck.html'))
    # path('dogs/', views.dogs_deck, name='dogs_deck'),
]

