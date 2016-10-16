"""
URLconf file
"""

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^create$', views.create_event, name='createevent'),
    url(r'^search$', views.search, name='search'),
]
