from django.contrib import admin
from watch_list.models import WatchList, StreamPlatform, Reviews


# Register your models here.
admin.site.register(WatchList)
admin.site.register(StreamPlatform)
admin.site.register(Reviews)
