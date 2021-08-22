from django.urls import path

from .views import base_views

app_name = 'index'

urlpatterns = [
    path('ranking_outer', base_views.ranking_outer, name='ranking_outer'),
    path('ranking_pants', base_views.ranking_pants, name='ranking_pants'),
    path('analysis', base_views.intro, name='data'),
    path('', base_views.search, name='search'),
]