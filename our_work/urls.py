from django.urls import path
from .views import *


app_name = "our_work"

urlpatterns = [
    path("digital-singles", digital_singles, name="digital_singles"),
    path("music-covers", music_covers, name="music_covers"),
    path("official-music-videos", official_music_videos, name="official_music_videos"),
    path("video-production", video_production, name="video_production"),
    path("talent-management", talent_management, name="talent_management"),
    path("talent-management/<str:person>", talent_management, name="talent"),
    path("stage-performance", stage_performance, name="stage_performance"),
    path("branded-content", branded_content, name="branded_content"),
    path("influencer-marketing", influencer_marketing, name="influencer_marketing"),
    path("", home, name="home")
]