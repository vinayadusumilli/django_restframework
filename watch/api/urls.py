from django.contrib import admin
from django.urls import path, include
import watch_app.urls
import user_app.api.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('watch/', include(watch_app.urls)),
    path('username/', include(user_app.api.urls))

]
