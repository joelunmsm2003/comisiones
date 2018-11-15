# -*- coding: utf-8 -*-
#    ___       ___       ___       ___            ___       ___   
#   /\  \     /\__\     /\  \     /\__\          /\  \     /\  \  
#  /  \  \   / | _|_   /  \  \   |  L__L        _\ \  \   /  \  \ 
# /  \ \__\ /  |/\__\ / /\ \__\  |   \__\      /\/  \__\ / /\ \__\
# \/\  /  / \/|  /  / \ \/ /  /  /   /__/      \  /\/__/ \ \/ /  /
#   / /  /    | /  /   \  /  /   \/__/          \/__/     \  /  / 
#   \/__/     \/__/     \/__/                              \/__/

# email : joelunmsm@gmail.com
# web   : xiencias.com

from django.shortcuts import *
from django.template import RequestContext
from django.contrib.auth import *
from django.views.generic import View
from django.contrib.auth.models import Group, User
from django.core import serializers
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.models import Group, User
from jwt_auth.compat import json
from jwt_auth.mixins import JSONWebTokenAuthMixin
from django.template import RequestContext
import simplejson
from django.views.decorators.csrf import csrf_exempt
import xlrd
from django.db.models import Count,Sum
from app.models import *
from app.forms import *
from app.serializers import *
from django.db.models import Count,Sum
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth import authenticate
import time
from django.db.models import Func
import os
from datetime import datetime,timedelta,date
import os.path
import requests
import smtplib
from email.mime.text import MIMEText
from django.db.models import Count,Max
import datetime
import random
from django.db.models import Count,Sum
from PIL import Image
from resizeimage import resizeimage
#import unicodecsv as csv
import pandas as pd


def opcionagente(request):

	a = Agente.objects.all()
	#recetas = Receta.objects.all()
	context = {'agentes':a,'tetas':'besitos'}

	return render(request, 'menu_agentes.html', context)

def agente_poliza(request,agente):

	if request.method=='POST':

		form = PolizaForm(request.POST)

		if form.is_valid():

			form.save()

			return HttpResponseRedirect('/poliza/'+str(agente))


	if request.method=='GET':

		p=Poliza(agente_id=agente)

		form = PolizaForm(instance=p)

		_polizas= Poliza.objects.filter(agente_id=agente)

		context = {'polizas':_polizas,'agente':agente,'form':form}

		return render(request, 'agente_poliza.html', context)

def detalleagente(request,agente):

	if request.method=='POST':

		a = Agente.objects.get(id=agente)

		form = AgenteForm(request.POST,instance=a)

		if form.is_valid():

			form.save()

			return HttpResponseRedirect('/detalleagente/'+str(agente))


	if request.method=='GET':

		a = Agente.objects.get(id=agente)

		form = AgenteForm(instance=a)

		context = {'agente':a,'form':form,'agente':agente}

		return render(request, 'detalle_agente.html', context)


def opcionproducto(request):

	a = Producto.objects.all()
	#recetas = Receta.objects.all()
	context = {'producto':a}

	return render(request, 'menu_productos.html', context)


def agrega_agente(request):

	if request.method=='POST':

		form = AgenteForm(request.POST)

		if form.is_valid():

			form = AgenteForm(request.POST).save()

			return HttpResponseRedirect('/opcionagente/')

	if request.method=='GET':


		form = AgenteForm()

		context = {'form':form}

		return render(request, 'agrega_agente.html', context)


def opcionpoliza(request):

	p = Poliza.objects.all()
	#recetas = Receta.objects.all()
	context = {'poliza':p}


	return render(request, 'menu_poliza.html', context)



def mobile(request):
	"""Return True if the request comes from a mobile device."""
	MOBILE_AGENT_RE=re.compile(r".*(iphone|mobile|androidtouch)",re.IGNORECASE)
	if MOBILE_AGENT_RE.match(request.META['HTTP_USER_AGENT']):
		return True
	else:
		return False

def ValuesQuerySetToDict(vqs):

	return [item for item in vqs]










def ingresar(request):

	
	return render(request, 'ingresar.html',{})

def polizas(request):


	r=Poliza.objects.all().values('numero_poliza','cliente__agente__nombre','cliente__agente__photo','cliente__agente__apellidos','cliente__dni','cliente__telefono','cliente__nombre','cliente__agente__nombre','cliente__agente__apellidos','producto__ramo_compania_producto__ramo__nombre','producto__ramo_compania_producto__compania__nombre','producto__ramo_compania_producto__compania__nombre','producto__ramo_compania_producto__producto__nombre')

	# for i in range(len(r)):

	# 	p =Cliente.objects.filter(cliente_id=r[i]['id']).values('id','numero_poliza')

	# 	r[i]['poliza']= ValuesQuerySetToDict(p)

	r= simplejson.dumps(ValuesQuerySetToDict(r))
	return HttpResponse(r, content_type="application/json")

def agentes(request):


	_agentes = Agente.objects.all()
	serializer = AgenteSerializer(_agentes, many=True)
	return JsonResponse(serializer.data, safe=False)




def _jerarquia(request,agente):

	__jerarquia = Agentejerarquia.objects.filter(agente_id=agente)
	serializer = AgentejerarquiaSerializer(__jerarquia, many=True)
	return JsonResponse(serializer.data, safe=False)


def clientes(request):


	r=Cliente.objects.all().values('id','nombre','apellido').order_by('id')
	r= simplejson.dumps(ValuesQuerySetToDict(r))
	return HttpResponse(r, content_type="application/json")


def apicliente(request,id_cliente):


	r=Cliente.objects.filter(id=id_cliente).values('id','nombre','apellido','email','telefono','direccion','estado_civil','numero_hijos','agente','dni','conyuge','edad_conyuge')

	for i in range(len(r)):

		p =Poliza.objects.filter(cliente_id=r[i]['id']).values('id','numero_poliza')

		r[i]['poliza']= ValuesQuerySetToDict(p)

	r= simplejson.dumps(ValuesQuerySetToDict(r))
	
	return HttpResponse(r, content_type="application/json")

def dashboard(request):

	
	return render(request, 'dashboard.html',{})

def menu(request):

	
	return render(request, 'menu.html',{})


def listaramos_1(request):

	r=Ramo.objects.all().values('id','nombre')
	r= simplejson.dumps(ValuesQuerySetToDict(r))
	return HttpResponse(r, content_type="application/json")


def listacia_1(request,ramo):


	r=RamoCompaniaProducto.objects.filter(ramo_id=ramo).values('compania','compania__nombre').exclude(antiguo=1).annotate(c=Max('compania')).order_by('compania')
	r= simplejson.dumps(ValuesQuerySetToDict(r))
	return HttpResponse(r, content_type="application/json")


def listaproductos(request,cia):

		r=RamoCompaniaProducto.objects.filter(compania_id=cia).exclude(antiguo=1).values('id','producto','producto__nombre')
		r= simplejson.dumps(ValuesQuerySetToDict(r))
		return HttpResponse(r, content_type="application/json")

def polizanueva(request):

	
	return render(request, 'polizanueva.html',{})

def opcionagentes(request):


	
	return render(request, 'menuagentes.html',{})


def polizaexistente(request):

	
	return render(request, 'polizaexistente.html',{})




def sacasemana(fecha):



	s = fecha
	args = time.strptime(s, "%Y-%m-%d")[:3]
	date = datetime.date(*args)
	weeknum = date.isocalendar()[1]

	return weeknum






class Month(Func):
	function = 'EXTRACT'
	template = '%(function)s(MONTH from %(expressions)s)'
	output_field = models.IntegerField()    








@csrf_exempt
def subirarchivo(request):


	df = pd.read_csv('/home/capital/pos_julio_enero_2019_ecuador_xxx.csv')

	base = []

	todos = []

	asesor_anterior= ''

	for i in range(df.shape[0]):

		#Agente


		asesor_anterior = df['Asesor Inicial'][i]

		asesor = df['Asesor Responsable'][i]

		dni = df['ID']


		a = Agente.objects.filter(user__username__contains=asesor)

		if a.count()>0:

			age = a[0].id


		#Cliente

		clien = df['Cliente'][i]

		ramo = df['Ramo'][i]

		compania = df['Compana'][i]

		producto = df['Producto'][i]

		

		rcp = RamoCompaniaProducto.objects.filter(ramo__nombre=ramo,compania__nombre=compania,producto__nombre=producto)

	

		numero_poliza=df['Poliza'][i]

		fecha_poliza=df['Fecha Vigencia'][i]

		_modalidad = df['Modalidad'][i]

		## Si el cliente existe

		if Cliente.objects.filter(nombre=clien).count() > 0:

			#
			id_cliente = Cliente.objects.get(nombre=clien).id

		else:

			##

			Cliente(agente_id=age,nombre=clien,upload_ene_jul_2019_ecu=1,dni=dni).save()

			id_cliente=Cliente.objects.all().values('id').order_by('-id')[0]['id']


		# '_modalidad',_modalidad,type(_modalidad)

		if _modalidad:

			_modalidad = str(_modalidad).capitalize()

		else:

			_modalidad = 'Anual'

		mo = Modalidad.objects.filter(nombre__contains=_modalidad)

		# _modalidad,mo

		if mo.count()>0:

			modalidaddato = mo[0].id




		fecha_poliza = datetime.datetime.strptime(fecha_poliza, '%m/%d/%Y')
		
		status = df['Estatus'][i]

		ss =Statuspoliza.objects.filter(nombre__contains=status)

		if ss.count()>0:

			es = ss[0].id

		else:

			es=1

		PropuestaCliente(cliente_id=id_cliente,ramo_compania_producto_id=rcp[0].id,agente_id=age,upload_csv_julio_enero_2019=1,fecha=fecha_poliza).save()

		id_propuesta=PropuestaCliente.objects.all().values('id').order_by('-id')[0]['id']

		Citas(tipo_cita_id=2,tipo_seguimiento_id=2,cliente_id=id_cliente,propuesta_cliente_id=id_propuesta,agente_id=age,numero_poliza=numero_poliza,fecha_poliza=fecha_poliza,status_poliza_id=es,cliente_antiguo='Yes',upload_ene_jul_2019_ecu=1,fecha_cita=fecha_poliza,modalidad_id=modalidaddato,asesor_anterior=asesor_anterior).save()

		Citas(tipo_cita_id=3,tipo_seguimiento_id=4,cliente_id=id_cliente,propuesta_cliente_id=id_propuesta,agente_id=age,numero_poliza=numero_poliza,fecha_poliza=fecha_poliza,status_poliza_id=es,cliente_antiguo='Yes',upload_ene_jul_2019_ecu=1,fecha_cita=fecha_poliza,modalidad_id=modalidaddato,asesor_anterior=asesor_anterior).save()


	

	return HttpResponse('ok', content_type="application/json")





