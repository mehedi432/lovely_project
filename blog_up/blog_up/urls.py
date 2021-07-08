from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Dellab | Blog"
admin.site.site_title = "Dellab | Blog"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),

    path('', include('main.urls')),
    path('', include('blog.urls')),
]
