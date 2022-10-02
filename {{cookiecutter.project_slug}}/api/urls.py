from api.v1 import urlpatterns as v1_urlpatterns
from django.urls import path, include

urlpatterns = [
    path('/v1', include(v1_urlpatterns)),
]
