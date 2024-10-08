from django.contrib import admin
from django.urls import path, include
from movie_list import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movie/', include(urls))

]
