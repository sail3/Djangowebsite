from django.conf.urls import patterns, include, url
from django.contrib import admin
from DjangoWebsite.views import current_datetime, home

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DjangoWebsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$',home),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hora-servidor/$', current_datetime),
)
