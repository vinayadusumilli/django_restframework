from django.urls import path
from watch_app.api.views import (WatchListAV, WatchDetailAV,
                                 StreamPlatformAV, PlatformAV, ReviewList
                                 ,ReviewDetail)
# from watch_app.api.views import movies_list, watch_list

urlpatterns = [
    path('', WatchListAV.as_view(), name='watch_list'),
    path('<int:pk>', WatchDetailAV.as_view(), name='watch_detail'),
    path('platforms', StreamPlatformAV.as_view(), name='stream_platform'),
    path('platform/<int:pk>', PlatformAV.as_view(), name='stream_platform_detail'),
    path('reviews', ReviewList.as_view(), name='review_list'),
    path('review/<int:pk>', ReviewDetail.as_view(), name='review_detail')



    #path('<int:pk>/reviews', WatchDetailAV.as_view(), name='movies_reviews'),
]
