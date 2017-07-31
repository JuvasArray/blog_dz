from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.conf.urls.static import static
from blog.sitemaps import PostSitemap
from django.conf import settings

sitemaps = {
    'posts': PostSitemap,
}

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^ckeditor', include('ckeditor_uploader.urls')),
    url(r'^blog/', include('blog.urls', namespace='blog', app_name='blog')),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]

if settings.DEBUG is True:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
