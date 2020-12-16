from django.urls import path
from .views import *


app_name = "our_work"

urlpatterns = [
    path("", home, name="home")
]