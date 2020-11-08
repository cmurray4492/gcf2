from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
]

"""
urlpatterns = [
    path('tinymce/', include('tinymce.urls')),

    path('blog/', include('srwblog.urls')),
    path('chruches/', include('chruches.urls')),
    path('prayers/', include('prayers.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
""" 