from api.v1.urls import urlpatterns as v1_urlpatterns
from django.urls import include, path

app_name = "api"


urlpatterns = [
    path("/v1", include(v1_urlpatterns)),
]
