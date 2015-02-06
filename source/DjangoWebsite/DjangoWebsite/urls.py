from django.conf.urls import patterns, include, url
from django.contrib import admin
from DjangoWebsite.views import current_datetime, home, nosotros, generar_lista, mostrar_datos, prototype

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DjangoWebsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$',home),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hora-servidor/$', current_datetime),
    url(r'^nosotros/$', nosotros),
    url(r'^lista/(\d{1,2})/$', generar_lista),
    url(r'^datos/(\w+)/(\w+)/(\w+)/$', mostrar_datos),
    url(r'^prototipo$', prototype)
    # url(r'^consulta_db/$', user_list),
)
