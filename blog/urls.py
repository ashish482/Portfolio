from django.conf.urls import url
from django.conf import settings
from . import views
from django.contrib.staticfiles.urls import static

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^blog/', views.blog, name='blog'),
    url(r'^read/(?P<slug>[\w-]+)/$', views.post, name='post'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)