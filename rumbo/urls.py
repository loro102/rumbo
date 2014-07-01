# encoding: utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

# noinspection PyPep8
admin.autodiscover ()

# noinspection PyPep8
urlpatterns = patterns ('',
                        # Examples:
                        # url(r'^$', 'rumbo.views.home', name='home'),
                        # url(r'^blog/', include('blog.urls')),
                        # Aqui iran todos los enlaces del programa
                        # url (r'^$', 'principal.views.inicio'),
                        # ################################### Clientes ###########################################
                        url (r'^cliente/listado/$', 'principal.views.lista_clientes'),
                        # Enlace para listado de clientes
                        url (r'^cliente/detalle/(?P<cliente_id>\d+)', 'principal.views.cliente_detalle'),
                        # enlace detalle cliente
                        url (r'^cliente/nuevo/$', 'principal.views.nuevo_cliente'),
                        #Enlace para clientes nuevos

                        # ##################################### Agentes ##########################################
                        url (r'^agente/nuevo/$', 'principal.views.nuevo_agente'),
                        # Enlace para insertar agentes nuevos

                        # ########################################## Siniestros ###################################

                        url (r'^siniestro/detalle/(?P<siniestro_id>\d+)', 'principal.views.siniestro_detalle'),
                        # enlace detalle siniestro
                        url (r'^siniestro/nuevo/(?P<cliente_id>\d+)', 'principal.views.nuevo_siniestro'),
                        # enlace para insertar siniestros

                        ########################################### Aseguradoras ################################
                        url (r'^aseguradora/nuevo/$', 'principal.views.nueva_aseguradora'),
                        # enlace para insertar aseguradoras
                        url (r'^tramitadorcia/nuevo/(?P<aseguradora_id>\d+)', 'principal.views.nuevo_tramitadorcia'),
                        # enlace para insertar tramitadores de las aseguradoras

                        ############################################ Profesionales ###############################
                        url (r'^profesional/nuevo/$', 'principal.views.nuevo_profesional'),
                        # enlace para insertar profesionales

                        ############################################ Otros #######################################
                        url (r'^chaining/', include ('smart_selects.urls')),
                        #Enlace para ajax de los selects dependientes dinamicos
                        url (r'^admin/', include (admin.site.urls)), )
# Enlace para administracion
# Configuracion para servir la carpeta Static
if settings.DEBUG and settings.STATIC_ROOT: urlpatterns += patterns ('', (
r'%s(?P<path>.*)$' % settings.STATIC_URL.lstrip ('/'), 'django.views.static.serve',
{'document_root': settings.STATIC_ROOT}), )