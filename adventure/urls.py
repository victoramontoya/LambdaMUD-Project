from django.conf.urls import url
from . import api
from rest_framework import routers
from django.urls import path, include, re_path
from adventure.api import PersonalNoteViewSet


router = routers.DefaultRouter()
router.register(r'adventure', AdventureViewSet)


urlpatterns = [
    url('init', api.initialize),
    url('move', api.move),
    url('say', api.say),
]