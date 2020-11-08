from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('blog/', include('gcfblog.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""
urlpatterns = [
    path('tinymce/', include('tinymce.urls')),


    path('chruches/', include('chruches.urls')),
    path('prayers/', include('prayers.urls')),
] 
""" 