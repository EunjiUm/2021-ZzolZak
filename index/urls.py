from django.urls import path

from .views import base_views

app_name = 'index'

urlpatterns = [
    path('ranking', base_views.ranking, name='ranking'),
    path('analysis', base_views.intro, name='data'),
    path('', base_views.search, name='search'),
    path('about', base_views.about, name='about'),
]