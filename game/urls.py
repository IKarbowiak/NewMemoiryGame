from django.urls import path
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path('', views.start_site, name='start_site'),
    path(r'dogs/', TemplateView.as_view(template_name='game/dogs_deck.html'))
    # path('dogs/', views.dogs_deck, name='dogs_deck'),
]

