from django.contrib import admin
from django.urls import path, include
from watch_list import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(urls))

]
