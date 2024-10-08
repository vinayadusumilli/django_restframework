from django.urls import path
from movie_app.api.views import movies_list, movie_list

urlpatterns = [
    path('list/', movies_list, name='movies_list'),
    path('<int:pk>', movie_list, name='movie_list'),

]
