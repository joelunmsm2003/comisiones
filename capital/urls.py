
#from django.conf.urls import patterns, include, url
from django.conf.urls import url

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from app.views import *

from django.contrib import admin


admin.site.site_header = 'Capital'
from app.admin import admin_site

urlpatterns = [

    url(r'opcionagentes/', opcionagentes),
    url(r'^admin/', admin.site.urls),
    url(r'api-token-auth/', obtain_jwt_token),
    url(r'api-token-refresh/', refresh_jwt_token),

    url(r'^pos/', admin_site.urls),


    url(r'ingresar/', ingresar),
    url(r'polizas/', polizas),
    url(r'polizanueva/', polizanueva),
    url(r'polizaexistente/', polizaexistente),
    url(r'menu/', menu),
    url(r'agentes/', agentes),
    url(r'opcionagente/', opcionagente),
    url(r'opcionpoliza/', opcionpoliza),
    url(r'opcionproducto/', opcionproducto),
    url(r'agente/(\d+)', detalleagente),
    url(r'poliza/(\d+)', agente_poliza),
    url(r'agrega_agente/', agrega_agente),


    url(r'clientes/', clientes),

    url(r'dashboard/', dashboard),
    url(r'^listaramos_1/$', listaramos_1),
    url(r'^listacia_1/(\d+)$', listacia_1),
    url(r'^listaproductos/(\d+)$', listaproductos),

    url(r'apicliente/(\d+)', apicliente),


]
