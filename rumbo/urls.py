#encoding: utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rumbo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	#Aqui iran todos los enlaces del programa
	url(r'^$','principal.views.lista_clientes'),
	url(r'^cliente/nuevo/$','principal.views.nuevo_cliente'),#Enlace para insertar clientes nuevos
	url (r'^agente/nuevo/$', 'principal.views.nuevo_agente'),  # Enlace para insertar clientes nuevos
	url(r'^siniestro/nuevo/(?P<cliente_id>\d+)','principal.views.nuevo_siniestro'),#enlace para insertar siniestros
    url(r'^admin/', include(admin.site.urls)),
)#Configuracion para servir la carpeta Static
if settings.DEBUG and settings.STATIC_ROOT:
    urlpatterns += patterns('',
        (r'%s(?P<path>.*)$' % settings.STATIC_URL.lstrip('/'),
            'django.views.static.serve',
            {'document_root' : settings.STATIC_ROOT }),)
