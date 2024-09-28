from django.urls import path
from .view import WatchListAV, WatchDetailAV, StreamPlatformAV, StreamPlatformDetailAV

urlpatterns = [
    path("list/", WatchListAV.as_view(), name="watch-list"),
    path("list/<int:pk>/", WatchDetailAV.as_view(), name="watch-detail"),
    path("platform/", StreamPlatformAV.as_view(), name="stream-platform"),
    path("platform/<int:pk>/", StreamPlatformDetailAV.as_view(), name="stream-platform-detail"),
]