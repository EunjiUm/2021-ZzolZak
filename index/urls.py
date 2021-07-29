from django.urls import path

from .views import base_views

app_name = 'index'

urlpatterns = [
    path('test', base_views.index, name='index'),
    path('', base_views.intro, name='data'),
]