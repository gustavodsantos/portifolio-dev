from django.urls import path

from mysite.base.views import apresentation, home

app_name = 'base'
urlpatterns = [
    path('', home, name='home'),
    path('base/', apresentation, name='apresentation'),
]
