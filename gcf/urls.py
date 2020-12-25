from django.contrib import admin
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import path, include
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('blog/', include('gcfblog.urls')),
    path('ads.txt', RedirectView.as_view(url=staticfiles_storage.url("ads.txt"))),
    path('sitemap.xml', RedirectView.as_view(url=staticfiles_storage.url("sitemap.xml"))),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""
urlpatterns = [
    path('chruches/', include('chruches.urls')),
    path('prayers/', include('prayers.urls')),
"""
