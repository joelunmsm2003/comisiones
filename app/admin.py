from django.contrib import admin
from app.models import *
from django.forms import *
from django.contrib.admin import RelatedOnlyFieldListFilter
from daterange_filter.filter import DateRangeFilter
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from PIL import Image
from resizeimage import resizeimage
import os.path
import json
import requests
from django.contrib import admin
from django.contrib.admin.filters import DateFieldListFilter
import xlwt
from datetime import datetime
import csv
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter
from django.utils.html import format_html
from django.core.urlresolvers import reverse
from django.conf.urls import url
from import_export.admin import ImportExportModelAdmin


@admin.register(Comision)
class ComisionAdmin(admin.ModelAdmin):
	list_display = ('id','datocomision','comision','tipo_agente')
	list_filter =('tipo_agente','datocomision')



@admin.register(Datocomision)
class DatocomisionAdmin(admin.ModelAdmin):
	list_display = ('producto','rango_inicio','rango_fin','pca_l1','pca_l2','senior_pca','relationship_manager','relationship_manager_senior','relationship_director','bussiness_partner')
	list_filter= ('producto__ramo','producto__compania')
	list_editable=('pca_l1','pca_l2','senior_pca','relationship_manager','relationship_manager_senior','relationship_director','bussiness_partner')



class MyAdminSite(AdminSite):
    site_header = 'POS Administrador'

admin_site = MyAdminSite(name='myadmin')


# @admin.register(Statuspoliza)
# class StatuspolizaAdmin(admin.ModelAdmin):
#     list_display = ('id','nombre')
#     list_editable = ('nombre',)

@admin.register(Poliza)
class PolizaAdmin(admin.ModelAdmin):
    list_display = ('id','agente','ramo_compania_producto','numero_poliza','fecha','fecha_emision')
    list_editable = ('fecha_emision',)
    list_filter = ('cliente__estado_civil','agente')
    actions = ['listar',]


    def listar(self,request,queryset):


    	print request.GET

    	for q in queryset:

    		print q.codigo



# @admin.register(Nivel)
# class NivelAdmin(admin.ModelAdmin):
#     list_display = ('id','nombre','descripcion')
#     list_editable = ('nombre',)

# @admin.register(TipoAgente)
# class TipoAgenteAdmin(admin.ModelAdmin):
#     list_display = ('id','nombre')
#     list_editable = ('nombre',)

# @admin.register(Grupo)
# class GrupoAdmin(admin.ModelAdmin):
# 	list_display = ('id','nombre')
# 	list_editable = ('nombre',)

# @admin.register(Subgrupo)
# class SubgrupoAdmin(admin.ModelAdmin):
# 	list_display = ('id','nombre')
# 	list_editable = ('nombre',)


# @admin.register(Mes)
# class MesAdmin(admin.ModelAdmin):
#     list_display = ('id','nombre')
#     list_editable = ('nombre',)




# @admin.register(Compania)
# class CompaniaAgenteAdmin(admin.ModelAdmin):
# 	list_display = ('id','nombre')
# 	list_editable = ('nombre',)

# @admin.register(Producto)
# class ProductoAdmin(admin.ModelAdmin):
# 	list_display = ('id','nombre')
# 	list_editable = ('nombre',)

# @admin.register(Ramo)
# class RamoAdmin(admin.ModelAdmin):
# 	list_display = ('id','nombre')
# 	list_editable = ('nombre',)


# @admin.register(Jerarquia)
# class JerarquiaAdmin(admin.ModelAdmin):
# 	list_display = ('id','nombre')
# 	list_editable = ('nombre',)

# @admin.register(TipoCita)
# class TipoCitaAdmin(admin.ModelAdmin):
#     list_display = ('id','nombre')
#     list_editable = ('nombre',)

# @admin.register(TipoSeguimiento)
# class TipoSeguimientoAdmin(admin.ModelAdmin):
#     list_display = ('id','nombre')
#     list_editable = ('nombre',)

# @admin.register(Relacion)
# class RelacionAdmin(admin.ModelAdmin):
#     list_display = ('id','nombre')
#     list_editable = ('nombre',)


# @admin.register(TipoAgente)
# class TipoAgenteAdmin(admin.ModelAdmin):
#     list_display = ('id','nombre')
#     list_editable = ('nombre',)

    
def bulksms(audience):

	url ="http://smsbulk.pe/SmsBulk/rest/ws/bulkSms"
	username = 'xiencias'
	password = '9nG4SB'


	for recipient in audience:
		
		phone_number = recipient

		message = audience[recipient]

		if phone_number[:3] == '+51':

			phone_number = phone_number[1:12]

		else:

			if phone_number[:2] != '51':

				phone_number = '51%s' % phone_number





		params = {'usr' : username,'pas' : password,'msg' : message ,'num' : phone_number}



		reply = requests.get(url, params=params)

		result1 = reply.text

		return result1



class AgenteListFilter(admin.SimpleListFilter):
	# Human-readable title which will be displayed in the
	# right admin sidebar just above the filter options.
	title ='Agente'

	# Parameter for the filter that will be used in the URL query.
	parameter_name = 'Usuario'

	def lookups(self, request, model_admin):
		"""
		Returns a list of tuples. The first element in each
		tuple is the coded value for the option that will
		appear in the URL query. The second element is the
		human-readable name for the option that will appear
		in the right sidebar.
		"""
		return (
			('X', 'X'),
			# ('90s', 'in the nineties'),
		)

	def queryset(self, request, queryset):


		try:

			grupo = User.objects.get(pk=request.user.id).groups.get()

			equipo = Agente.objects.get(user_id=request.user.id).equipo.nombre



			if str(grupo)=='PRIVATE CLIENT ADVISOR':

				return queryset.filter(user_id=request.user.id)

			if str(grupo)=='GERENTE' or str(grupo)=='DIRECTOR' or str(grupo)=='GERENTE GENERAL' or str(grupo)=='GERENTE' :

				return queryset.filter(equipo__nombre=equipo)


			if str(grupo)=='ADMIN':

				return queryset.all()

		except:

			return queryset.all()






@admin.register(Agente)
class AgenteAdmin(ImportExportModelAdmin):

	list_display=('id','pais','nombre','apellidos','tipo_agente','correo_capital','telefono','detalle')
	list_filter = (('tipo_agente__nombre', DropdownFilter),('pais__nombre', DropdownFilter))
	search_fields = ('id','nombre','user__username','apellidos')
	list_editable=('telefono',)
	exclude=('hispana_seguros','fpi','gi','bmiec_salud','cfp','mapfre','equinoccial','qbe','chubb','liberty','it','bupa','bmi_health','pc','paiic','nwl','bmi_lif')
	actions = ['envia_alerta','envia_notificacion_actualizacion']


	def detalle(self, obj):

		print self
		print '.....'
		print obj.id
		return format_html(
			'<a class="button related-widget-wrapper-link add-related" href="/agente/'+str(obj.id)+'&_popup=1">Ver</a>'
		)




	def envia_alerta(self, request,queryset):

		for a in queryset:


			plantillas = Mensaje.objects.filter(activado=1)

			for msj in plantillas:

				if msj.notificacion==1:

					envia_notificacion(a.codigo,msj.contenido)

					Notificacion(agente_id=a.id,mensaje=msj.contenido).save()

				if msj.sms==1:

					mensaje=msj.contenido

					audience = {a.movil_contacto:mensaje}

					dato = bulksms(audience)


		return 'ok'



	def envia_notificacion_actualizacion(self, request,queryset):


		for a in queryset:


			header = {"Content-Type": "application/json; charset=utf-8",
					  "Authorization": "Basic ZTI5YjZhMWYtZTJkYS00OWJiLTkyZTAtMDRjMjIzOWNiOTBi"}

			payload = {"app_id": "ff177554-db1d-4280-bf67-5f5a7602ba5c",
					   "include_player_ids": [a.codigo],
					   "contents": {"en": 'Esto es un mensaje de prueba'}}
			 
			req = requests.post("https://onesignal.com/api/v1/notifications", headers=header, data=json.dumps(payload))
			 




		return 'ok'



	def save_model(self, request, obj, form, change):
		
		super(AgenteAdmin, self).save_model(request, obj, form, change)
		
		if Agente.objects.get(id=obj.id).photo:

			caption = '/home/capital/'+str(Agente.objects.get(id=obj.id).photo)
			fd_img = open(caption, 'r')
			img = Image.open(fd_img)
			width, height = img.size
			img = resizeimage.resize_cover(img, [300, 300])
			img.save(caption, img.format)
			fd_img.close()
	
	def usuario(self, obj):

		#grupo =User.objects.get(pk=id).groups.get()

		if obj.user:
			return obj.user.username
		else:
			return ''

	def tipo_agente(self, obj):

		if obj.tipo_agente:
			return obj.tipo_agente.nombre
		else:
			return ''
	def get_estructura(self, obj):
		
		if obj.estructura:
			return obj.estructura.nombre
		else:
			return ''

	def equipo(self, obj):
		
		if obj.equipo:
			return obj.equipo.nombre
		else:
			return ''

	def get_nivel(self, obj):
		
		if obj.nivel:
			return obj.nivel.nombre
		else:
			return ''

	def get_grupo(self, obj):
		
		if obj.grupo:
			return obj.grupo.nombre
		else:
			return ''

	def get_subgrupo(self, obj):
		
		if obj.subgrupo:
			return obj.subgrupo.nombre
		else:
			return ''


# @admin.register(Cliente)
# class ClienteAdmin(admin.ModelAdmin):
# 	list_display = ('id','cierre','nombre','apellido','agente','email','fecha_nacimiento','fecha_inicio')
# 	list_filter = ('upload_csv','agente','nombre','fecha_nacimiento')
# 	search_fields = ('nombre','email','telefono')

# 	def agente(self, obj):
# 		return obj.agente.nombre

# 	def cierre(self, obj):

# 		if Citas.objects.filter(cliente_id=obj.id,tipo_seguimiento__nombre='Cierre').count()>0:

# 			return 'Cierre'

# 		else:

# 			return '_'





# @admin.register(Agentejerarquia)
# class AgentejerarquiaAdmin(admin.ModelAdmin):
# 	list_display = ('id','agente','country_manager','nivel','bussiness_partner','relation_ship_director','relation_management','relation_management_senior','private_client','private_client_senior')
# 	list_filter=('agente','agente__pais__nombre')
# 	#list_editable=('bussiness_partner','relation_ship_director','relation_management','relation_management_senior','private_client','private_client_senior')
# 	search_fields=('agente__nombre','country_manager__nombre','bussiness_partner__nombre','relation_ship_director__nombre','relation_management__nombre','relation_management_senior__nombre','private_client__nombre','private_client_senior__nombre')

# 	def nivel(self, obj):
# 		return obj.agente.tipo_agente.nombre


# @admin.register(RamoCompaniaProducto)
# class RamoCompaniaProductoAdmin(admin.ModelAdmin):
# 	list_display = ('id','get_ramo','get_compania','get_producto','antiguo')
# 	list_filter = ('ramo__nombre','compania__nombre')
# 	list_editable=('antiguo',)
	
# 	def get_ramo(self, obj):
# 		return obj.ramo.nombre

# 	def get_compania(self, obj):
# 		return obj.compania.nombre

# 	def get_producto(self, obj):
# 		return obj.producto.nombre


