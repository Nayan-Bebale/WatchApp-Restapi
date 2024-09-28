from django.urls import path
from .view import (WatchListAV, WatchDetailAV,
                    StreamPlatformAV, StreamPlatformDetailAV, 
                    ReviewList, ReviewDetail, ReviewListCreate)

urlpatterns = [
    path("list/", WatchListAV.as_view(), name="watch-list"),
    path("list/<int:pk>/", WatchDetailAV.as_view(), name="watch-detail"),
    path("platform/", StreamPlatformAV.as_view(), name="stream-platform"),
    path("platform/<int:pk>/", StreamPlatformDetailAV.as_view(), name="stream-platform-detail"),

    # path("review/", ReviewList.as_view(), name="review-list"),
    # path("review/<int:pk>/", ReviewDetail.as_view(), name="review-detail"),

    path("platform/<int:pk>/review-create/", ReviewListCreate.as_view(), name="review-list"),
    path("platform/<int:pk>/review/", ReviewList.as_view(), name="review-list"),
    path("platform/review/<int:pk>/", ReviewDetail.as_view(), name="review-detail"),
]