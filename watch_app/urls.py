from django.urls import path
from watch.api.views import (WatchLists, WatchDetail,
                             StreamPlatformAV, PlatformAV, ReviewList
                                 , ReviewDetail, ReviewCreate)
# from watch.api.views import movies_list, watch_app

urlpatterns = [
    path('', WatchLists.as_view(), name='watch_app'),
    path('<int:pk>', WatchDetail.as_view(), name='watch_detail'),
    path('platforms', StreamPlatformAV.as_view(), name='stream_platform'),
    path('platform/<int:pk>', PlatformAV.as_view(), name='stream_platform_detail'),
    path('reviews', ReviewList.as_view(), name='review_list'),
    path('review/<int:pk>', ReviewDetail.as_view(), name='review_detail'),
    path('<int:pk>/reviews', ReviewList.as_view(), name='watch_reviews'),
    path('<int:pk>/create_reviews', ReviewCreate.as_view(), name='create_reviews')



    #path('<int:pk>/reviews', WatchDetailAV.as_view(), name='movies_reviews'),
]
