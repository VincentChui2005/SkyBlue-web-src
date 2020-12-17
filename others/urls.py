from django.urls import path
from .views import home, load_static, about_us, our_client, link, contact_us, join_us


app_name = "others"

urlpatterns = [
    path("about-us", about_us, name="about_us"),
    path("our_client", our_client, name="our_client"),
    path("link", link, name="link"),
    path("contact-us", contact_us, name="contact_us"),
    path('join-us', join_us, name="join_us"),
    path("static/<path:filepath>", load_static, name="static"),
    path("", home, name="home"),
]