from django.urls import path
from app.views import *

urlpatterns = [
    path("sample/", SampleAPIView.as_view(), name="sample"),
]