from django.urls import path, include

from api.v1 import urlpatterns as v1_urlpatterns


urlpatterns = [
    path('/v1', include(v1_urlpatterns)),
]
