#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed=True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User
import datetime
from django.apps import AppConfig 



class Periodopos(models.Model):
    nombre = models.CharField(max_length=1000)

    class Meta:
        managed=True
        db_table = 'periodopos'
        verbose_name = 'Periodo POS'

    def __unicode__(self):
        return self.nombre

class Statuspoliza(models.Model):
    nombre = models.CharField(max_length=1000)

    class Meta:
        managed=True
        db_table = 'status_poliza'
        verbose_name = 'Status Poliza'

    def __unicode__(self):
        return self.nombre





class Estructura(models.Model):
    nombre = models.CharField(max_length=1000)

    class Meta:
        managed=True
        db_table = 'estructura'
        verbose_name = 'Estructura'

    def __unicode__(self):
        return self.nombre


class Jerarquia(models.Model):
    nombre = models.CharField(max_length=1000)
    nivel = models.ForeignKey('Nivel', models.DO_NOTHING, db_column='nivel', blank=True, null=True)

    class Meta:
        managed=True
        db_table = 'jerarquia'

    def __unicode__(self):
        return self.nombre

class Modalidad(models.Model):
    nombre = models.CharField(max_length=1000)

    class Meta:
        managed=True
        db_table = 'modalidad'
        verbose_name = 'Forma Pago'

    def __unicode__(self):
        return self.nombre



class Nivel(models.Model):
    nombre = models.CharField(max_length=1000)
    descripcion = models.CharField(max_length=1000,blank=True, null=True)

    class Meta:
        managed=True
        db_table = 'nivel'

    def __unicode__(self):
        return self.nombre

class Grupo(models.Model):
    nombre = models.CharField(max_length=1000)

    class Meta:
        managed=True
        db_table = 'grupo'

    def __unicode__(self):
        return self.nombre

class Mes(models.Model):
    nombre = models.CharField('Mes',max_length=1000)

    class Meta:
        managed=True
        db_table = 'mes'
        verbose_name ='Mes'

    def __unicode__(self):
        return self.nombre

class Subgrupo(models.Model):
    nombre = models.CharField(max_length=1000)

    class Meta:
        managed=True
        db_table = 'subgrupo'

    def __unicode__(self):
        return self.nombre

class TipoAgente(models.Model):
    nombre = models.CharField('Tipo de Agente',max_length=10000)

    class Meta:
        managed=True
        db_table = 'tipo_agente'
        verbose_name = 'Tipos de Agente'

    def __unicode__(self):
        return self.nombre


class EstadoCivil(models.Model):
    nombre = models.CharField(max_length=10000)

    class Meta:
        managed=True
        db_table = 'estado_civil'
        verbose_name = 'Estado Civil'

    def __unicode__(self):
        return self.nombre

class Agente(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING, db_column='user', blank=True, null=True)
    tipo_agente = models.ForeignKey('TipoAgente', models.DO_NOTHING, db_column='tipo_agente', blank=True, null=True)
    meta_personal = models.IntegerField(blank=True, null=True)
    meta_requerida = models.IntegerField(blank=True, null=True)
    meta_equipo = models.IntegerField(blank=True, null=True)
    fecha_ingreso = models.DateTimeField(blank=True, null=True)
    correo_capital = models.CharField(max_length=1000, blank=True, null=True)
    photo = models.FileField(upload_to='static',blank=True, null=True)
    estructura = models.ForeignKey('Estructura', models.DO_NOTHING, db_column='estructura', blank=True, null=True)
    equipo = models.ForeignKey('Equipo', models.DO_NOTHING, db_column='equipo', blank=True, null=True)
    pais = models.ForeignKey('Pais', models.DO_NOTHING, db_column='pais', blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    nombre = models.CharField(max_length=1000, blank=True, null=True)
    apellidos = models.CharField(max_length=1000, blank=True, null=True)
    nivel = models.ForeignKey('Nivel', models.DO_NOTHING, db_column='nivel',blank=True, null=True )
    #grupo = models.ForeignKey('Grupo', models.DO_NOTHING, db_column='grupo', blank=True, null=True)
    #subgrupo = models.ForeignKey('Subgrupo', models.DO_NOTHING, db_column='subgrupo', blank=True, null=True)
    dni = models.CharField(max_length=1000, blank=True, null=True)
    direccion = models.CharField(max_length=1000, blank=True, null=True)
    telefono = models.CharField(max_length=1000, blank=True, null=True)
    telefono_1 = models.CharField(max_length=1000, blank=True, null=True)
    relacion_contacto = models.CharField(max_length=1000, blank=True, null=True)
    telefono_contacto_emergencia = models.CharField(max_length=1000, blank=True, null=True)
    contacto_emergencia = models.CharField(max_length=1000, blank=True, null=True)
    correo_personal = models.CharField(max_length=1000, blank=True, null=True)
    movil_contacto = models.CharField(max_length=1000, blank=True, null=True)
    version = models.CharField(max_length=1000, blank=True, null=True)
    codigo = models.CharField(max_length=1000, blank=True, null=True)
    tipo_movil = models.CharField(max_length=1000, blank=True, null=True)
    grupo_prueba = models.ForeignKey('Agente', models.DO_NOTHING, db_column='grupo_prueba', blank=True, null=True)
    asesor_anterior = models.CharField(max_length=1000, blank=True, null=True)
    modelo = models.CharField(max_length=1000, blank=True, null=True)
    version_movil = models.CharField(max_length=1000, blank=True, null=True)


    cfp_ramo=models.BooleanField('Ramo CFP',default=False)
    ramos_generales=models.BooleanField(default=False)
    investments=models.BooleanField(default=False)
    salud=models.BooleanField(default=False)
    vida=models.BooleanField(default=False)


    hispana_seguros = models.BooleanField(default=False)
    fpi = models.BooleanField(default=False)
    gi = models.BooleanField(default=False)
    bmiec_salud = models.BooleanField(default=False)
    cfp = models.BooleanField(default=False)
    mapfre = models.BooleanField(default=False)
    equinoccial = models.BooleanField(default=False)
    qbe = models.BooleanField(default=False)
    chubb = models.BooleanField(default=False)
    liberty = models.BooleanField(default=False)
    it = models.BooleanField(default=False)
    bupa = models.BooleanField(default=False)
    bmi_health = models.BooleanField(default=False)
    pc = models.BooleanField(default=False)
    paiic = models.BooleanField(default=False)
    nwl = models.BooleanField(default=False)
    bmi_life = models.BooleanField(default=False)
    #agente_anterior = models.ForeignKey('Agente', models.DO_NOTHING, db_column='angente_anterior', blank=True, null=True)
    
    class Meta:
        managed=True
        db_table = 'agente'
        verbose_name = 'Agente'
        ordering = ('nombre',)

    def __unicode__(self):

        if self.user:
            return self.nombre + '  '+ self.apellidos
        else:
            return 'No tiene nombre'









class Semanas(models.Model):
    numero = models.CharField(max_length=1000)
    fecha_inicio = models.DateTimeField(blank=True, null=True)
    fecha_fin =  models.DateTimeField(blank=True, null=True)
    anio = models.CharField(max_length=1000)
    mes = models.ForeignKey('Mes', models.DO_NOTHING, db_column='mes',blank=True, null=True)

    class Meta:
        managed=True
        db_table = 'semanas'
        verbose_name = 'Semana'

    def __unicode__(self):

        if self.numero:

            return 'Semana '+str(self.numero) +' Mes '+str(self.mes)

        else:


            return ''



class Citas(models.Model):
    cliente = models.ForeignKey('Cliente', models.DO_NOTHING, db_column='cliente',blank=True, null=True)
    agente = models.ForeignKey('Agente', models.DO_NOTHING, db_column='agente',null=True)
    agente_cita_equipo = models.ForeignKey('Agente', models.DO_NOTHING, db_column='agente_cita_equipo',related_name='agente_cita_equipo', blank=True, null=True)
    tipo_cita = models.ForeignKey('TipoCita', models.DO_NOTHING, db_column='tipo_cita',null=True)
    propuesta_cliente = models.ForeignKey('PropuestaCliente', models.DO_NOTHING, db_column='propuesta_cliente',blank=True, null=True)
    tipo_seguimiento = models.ForeignKey('TipoSeguimiento', models.DO_NOTHING, db_column='tipo_seguimiento',null=True)
    fecha_cita = models.DateTimeField()
    observacion = models.CharField(max_length=10000,blank=True, null=True)
    fecha_solicitud = models.DateTimeField(blank=True, null=True)
    prima_target = models.CharField(max_length=1000,blank=True, null=True)
    modalidad = models.ForeignKey('Modalidad', models.DO_NOTHING, db_column='modalidad',blank=True, null=True)
    prima_anual = models.CharField(max_length=100,blank=True, null=True)
    fecha_poliza = models.DateTimeField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    semana = models.ForeignKey('Semanas', models.DO_NOTHING, db_column='semana',blank=True, null=True)
    inforce = models.BooleanField(default=False)
    agente_equipo = models.IntegerField(blank=True, null=True)
    numero_poliza = models.CharField('Numero Poliza',max_length=1000,blank=True, null=True)
    cliente_cita_equipo = models.CharField(max_length=1000, blank=True, null=True)
    propuesta_cita_equipo = models.CharField(max_length=1000, blank=True, null=True)
    cliente_antiguo = models.CharField(max_length=1000, blank=True, null=True,default='No')
    ramo_compania_producto = models.ForeignKey('RamoCompaniaProducto', models.DO_NOTHING, db_column='ramo_compania_producto', blank=True, null=True)
    status_poliza = models.ForeignKey('Statuspoliza', models.DO_NOTHING, db_column='status_poliza',default=1,blank=True, null=True)
    upload_csv = models.BooleanField(default=0)
    asesor_anterior = models.CharField(max_length=10000,blank=True, null=True)
    valida_pos = models.BooleanField(default=0)
    upload_csv_julio_enero_2019 = models.BooleanField(default=0)
    upload_ene_jul_2019_ecu=models.BooleanField(default=0)
    periodopos = models.ForeignKey('Periodopos', models.DO_NOTHING, db_column='periodopos',blank=True, null=True)
    

    class Meta:
        managed=True
        db_table = 'citas'
        verbose_name = 'Cita'
        ordering = ('agente',)

    def __unicode__(self):


        return self.tipo_cita.nombre




class Pos(models.Model):
    cliente = models.ForeignKey('Cliente', models.DO_NOTHING, db_column='cliente')
    agente = models.ForeignKey('Agente', models.DO_NOTHING, db_column='agente')
    tipo_cita = models.ForeignKey('TipoCita', models.DO_NOTHING, db_column='tipo_cita')
    propuesta_cliente = models.ForeignKey('PropuestaCliente', models.DO_NOTHING, db_column='propuesta_cliente')
    tipo_seguimiento = models.ForeignKey('TipoSeguimiento', models.DO_NOTHING, db_column='tipo_seguimiento')
    fecha_cita = models.DateField()
    observacion = models.CharField(max_length=10000,blank=True, null=True)
    fecha_solicitud = models.DateTimeField(blank=True, null=True)
    prima_target = models.IntegerField(max_length=1000,blank=True, null=True)
    modalidad = models.ForeignKey('Modalidad', models.DO_NOTHING, db_column='modalidad',blank=True, null=True)
    prima_anual = models.IntegerField(max_length=1000,blank=True, null=True)
    fecha_poliza = models.DateTimeField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    semana = models.ForeignKey('Semanas', models.DO_NOTHING, db_column='semana',blank=True, null=True)
    inforce = models.BooleanField()
    agente_equipo = models.IntegerField(blank=True, null=True)
    numero_poliza = models.CharField(max_length=1000,blank=True, null=True)
    upload_csv = models.BooleanField(default=0)
    status_poliza = models.ForeignKey('Statuspoliza', models.DO_NOTHING, db_column='status_poliza',default=1,blank=True, null=True)
    asesor_anterior = models.CharField(max_length=10000,blank=True, null=True)
    valida_pos = models.BooleanField(default=0)
    periodopos = models.ForeignKey('Periodopos', models.DO_NOTHING, db_column='periodopos',blank=True, null=True)

    
    

    class Meta:
        managed = False
        db_table = 'citas'
        verbose_name = 'POS'




class Cierres(models.Model):
    cliente = models.ForeignKey('Cliente', models.DO_NOTHING, db_column='cliente')
    agente = models.ForeignKey('Agente', models.DO_NOTHING, db_column='agente')
    tipo_cita = models.ForeignKey('TipoCita', models.DO_NOTHING, db_column='tipo_cita')
    propuesta_cliente = models.ForeignKey('PropuestaCliente', models.DO_NOTHING, db_column='propuesta_cliente')
    tipo_seguimiento = models.ForeignKey('TipoSeguimiento', models.DO_NOTHING, db_column='tipo_seguimiento')
    fecha_cita = models.DateField()
    observacion = models.CharField(max_length=10000,blank=True, null=True)
    fecha_solicitud = models.DateTimeField(blank=True, null=True)
    prima_target = models.CharField(max_length=1000,blank=True, null=True)
    modalidad = models.ForeignKey('Modalidad', models.DO_NOTHING, db_column='modalidad',blank=True, null=True)
    prima_anual = models.CharField(max_length=1000,blank=True, null=True)
    fecha_poliza = models.DateTimeField(blank=True, null=True)
    fecha_creacion = models.DateTimeField()
    semana = models.ForeignKey('Semanas', models.DO_NOTHING, db_column='semana',blank=True, null=True)
    inforce = models.BooleanField()
    agente_equipo = models.IntegerField(blank=True, null=True)
    numero_poliza = models.CharField(max_length=1000,blank=True, null=True)
    

    class Meta:
        managed = False
        db_table = 'citas'
        verbose_name = 'Cierre'



class Cliente(models.Model):
    #user = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='user', blank=True, null=True)
    nombre = models.CharField('Cliente',max_length=1000,blank=True, null=True)
    apellido = models.CharField(max_length=1000,blank=True, null=True)
    email = models.CharField(max_length=1000,blank=True, null=True)
    fecha_inicio = models.DateTimeField(blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    telefono = models.CharField(max_length=1000,blank=True, null=True)
    direccion = models.CharField(max_length=1000,blank=True, null=True)
    
    estado_civil = models.ForeignKey('EstadoCivil', models.DO_NOTHING, db_column='estado_civil', blank=True, null=True)
    numero_hijos = models.IntegerField(blank=True, null=True)
    agente = models.ForeignKey('Agente', models.DO_NOTHING, db_column='agente',null=True)
    #equipo = models.ForeignKey('Equipo', models.DO_NOTHING, db_column='equipo')
    dni = models.CharField(max_length=1000,blank=True, null=True)


    conyuge = models.CharField(max_length=1000,blank=True, null=True)
    edad_conyuge = models.IntegerField(blank=True, null=True)
    fecha_nacimiento_conyuge = models.DateField(blank=True, null=True)
    upload_csv=models.BooleanField(default=0)
    upload_csv_julio_enero_2019=models.BooleanField(default=0)
    upload_ene_jul_2019_ecu=models.BooleanField(default=0)
    

    class Meta:
        managed=True
        db_table = 'cliente'
        verbose_name = 'Cliente'
        ordering=('nombre',)


    def __unicode__(self):

        if self.nombre and self.apellido:
            return self.nombre + ' '+ self.apellido

        if self.nombre and self.apellido==None:
            return self.nombre

        else:
            return 'No tiene nombre'






class Compania(models.Model):
    nombre = models.CharField('Compania',max_length=1000, blank=True, null=True)

    class Meta:
        managed=True
        db_table = 'compania'
        verbose_name = 'Compania'

    def __unicode__(self):
        return self.nombre

class Equipo(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed=True
        db_table = 'equipo'
        verbose_name = 'Equipo'

    def __unicode__(self):
        return self.nombre






class Pais(models.Model):
    nombre = models.CharField(u'País',max_length=1000, blank=True, null=True)

    class Meta:
        managed=True
        db_table = 'pais'
        verbose_name = 'Paise'

    def __unicode__(self):
        return self.nombre


class Relacion(models.Model):
    nombre = models.CharField(max_length=1000)

    class Meta:
        managed=True
        db_table = 'relacion'


    def __unicode__(self):
        return self.nombre

class Mensaje(models.Model):
    nombre = models.CharField(max_length=1000,blank=True,null=True)
    subtitulo = models.CharField(max_length=1000,blank=True,null=True)
    contenido = models.CharField(max_length=1000,blank=True,null=True)
    fecha_programada =models.DateTimeField(blank=True,null=True)
    sms = models.BooleanField(default=0)
    notificacion = models.BooleanField(default=0)
    email = models.BooleanField(default=0)
    activado = models.BooleanField(default=0)

    class Meta:
        managed=True
        db_table = 'mensaje'


    def __unicode__(self):
        return self.nombre


class ParientesCliente(models.Model):
    cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='cliente',null=True)
    nombre = models.CharField(max_length=1000)
    edad = models.IntegerField(blank=True,null=True)
    fecha_nacimiento =models.DateTimeField(blank=True,null=True)
    relacion = models.ForeignKey('Relacion', models.DO_NOTHING, db_column='relacion', blank=True, null=True)

    class Meta:
        managed=True
        db_table = 'parientes_cliente'
        verbose_name = 'Parientes del Cliente'


class Producto(models.Model):
    nombre = models.CharField(max_length=1000)

    class Meta:
        managed=True
        db_table = 'producto'
        verbose_name = 'Producto'

    def __unicode__(self):
        return self.nombre




class Ramo(models.Model):
    nombre = models.CharField(max_length=10000)

    class Meta:
        managed=True
        db_table = 'ramo'

    def __unicode__(self):
        return self.nombre

class Agentejerarquia(models.Model):


    agente=models.ForeignKey(Agente, models.DO_NOTHING, db_column='agente',related_name='agente_asigna',verbose_name='Agente a asignar',default=142)
    country_manager = models.ForeignKey(Agente, models.DO_NOTHING, db_column='country_manager',related_name='country_manager',verbose_name='Country Manager',default=142)
    bussiness_partner = models.ForeignKey(Agente, models.DO_NOTHING, db_column='bussiness_partner',related_name='bussiness_partner',verbose_name='Business Partner',default=142)
    relation_ship_director = models.ForeignKey(Agente, models.DO_NOTHING, db_column='relation_ship_director',related_name='relation_ship_director',verbose_name='Relation Ship Director',default=142)
    relation_management = models.ForeignKey(Agente, models.DO_NOTHING, db_column='relation_management',related_name='relation_management',verbose_name='Relation Management',default=142)
    relation_management_senior = models.ForeignKey(Agente, models.DO_NOTHING, db_column='relation_management_senior',related_name='relation_management_senior',verbose_name='Relation Management Senior',default=142)
    private_client = models.ForeignKey(Agente, models.DO_NOTHING, db_column='private_client',related_name='private_client',verbose_name='Private Client',default=142)
    private_client_senior = models.ForeignKey(Agente, models.DO_NOTHING, db_column='private_client_senior',related_name='private_client_senior',verbose_name='Private Client Senior',default=142)
    class Meta:
        managed=True
        db_table = 'agentejerarquia'
        verbose_name = 'Agente / Jerarquia'

    def __unicode__(self):
        return self.agente.nombre
    @property
    def full_name(self):
        return self.agente.email






class RamoCompaniaProducto(models.Model):
    ramo = models.ForeignKey(Ramo, models.DO_NOTHING, db_column='ramo',null=True)
    compania = models.ForeignKey(Compania, models.DO_NOTHING, db_column='compania',null=True)
    producto = models.ForeignKey(Producto, models.DO_NOTHING, db_column='producto',null=True)
    antiguo = models.BooleanField(default=0)

    class Meta:
        managed=True
        db_table = 'ramo_compania_producto'
        ordering = ('ramo','compania','producto')

    def __unicode__(self):
        return self.ramo.nombre+' / '+self.compania.nombre+' / '+self.producto.nombre

class PropuestaCliente(models.Model):
    cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='cliente',null=True)
    agente = models.ForeignKey(Agente, models.DO_NOTHING, db_column='agente',null=True)
    observacion = models.CharField(max_length=10000)
    fecha = models.DateTimeField(blank=True, null=True)
    detalle = models.CharField(max_length=1000)
    ramo_compania_producto = models.ForeignKey('RamoCompaniaProducto', models.DO_NOTHING, db_column='ramo_compania_producto',null=True)
    inforce = models.BooleanField(default=False)
    interes = models.CharField(max_length=1000, blank=True, null=True)
    upload_csv=models.BooleanField(default=0)
    upload_csv_julio_enero_2019 = models.BooleanField(default=0)
    upload_ene_jul_2019_ecu=models.BooleanField(default=0)

    class Meta:
        managed=True
        db_table = 'propuesta_cliente'

    def __unicode__(self):
        return str(self.id)+'-'+self.ramo_compania_producto.ramo.nombre+' / '+self.ramo_compania_producto.compania.nombre+' / '+self.ramo_compania_producto.producto.nombre



class TelefonoUser(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING, db_column='user', blank=True, null=True)
    numero = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed=True
        db_table = 'telefono_user'
        verbose_name = 'Telefonos del Usuario'



class Estado(models.Model):
    nombre = models.CharField(max_length=1000)

    class Meta:
        managed=True
        db_table = 'estado'

    def __unicode__(self):
        return self.nombre




class TipoCita(models.Model):
    nombre = models.CharField(max_length=1000)

    class Meta:
        managed=True
        db_table = 'tipo_cita'
        verbose_name = 'Tipos de Cita'

    def __unicode__(self):
        return self.nombre


class TipoSeguimiento(models.Model):
    nombre = models.CharField(max_length=1000)

    class Meta:
        managed=True
        db_table = 'tipo_seguimiento'
        verbose_name = 'Tipos de Seguimiento'

    def __unicode__(self):
        return self.nombre


class Notificacion(models.Model):
    agente = models.ForeignKey(Agente, models.DO_NOTHING, db_column='agente', blank=True,null=True)
    nivel = models.ForeignKey(Nivel, models.DO_NOTHING, db_column='nivel', blank=True,null=True)
    pais = models.ForeignKey(Pais, models.DO_NOTHING, db_column='pais', blank=True,null=True)
    mensaje = models.TextField(max_length=10000, blank=True, null=True)
    fecha = models.DateTimeField(default=datetime.datetime.today())

    class Meta:
        managed=True
        db_table = 'notificacion'



class Agentecliente(models.Model):
    agente = models.ForeignKey(Agente, models.DO_NOTHING, db_column='agente',default=None)
    cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='cliente',default=None)

    class Meta:
        managed=True
        db_table = 'agentecliente'

class Iconos(models.Model):
    nombre = models.CharField(max_length=10000, blank=True, null=True)
    icono = models.CharField(max_length=10000, blank=True, null=True)

    class Meta:
        managed=True
        db_table = 'iconos'
        verbose_name = 'Icono'

    def __unicode__(self):
        return self.nombre


class Archivo(models.Model):

    TIPO_DOCUMENTO = (
        ('Formulario', 'Formulario'),
        ('Comercial', 'Comercial'),
    )
    ruta = models.FileField(upload_to='static',max_length=100000)
    #user = models.ForeignKey('AuthUser', models.DO_NOTHING, db_column='usuario')
    nombre =  models.CharField(blank=True, null=True,max_length=10000)
    #pais = models.ForeignKey('Pais', models.DO_NOTHING, db_column='pais', blank=True, null=True)
    ramo = models.ForeignKey(Ramo, models.DO_NOTHING, db_column='ramo',blank=True, null=True)
    compania = models.ForeignKey(Compania, models.DO_NOTHING, db_column='compania',blank=True, null=True)
    tipo_archivo = models.CharField(max_length=1000, choices=TIPO_DOCUMENTO)
    
    inhouse = models.BooleanField(default=False)
    broker = models.BooleanField(default=False)

    peru = models.BooleanField(default=False)
    ecuador = models.BooleanField(default=False)
    colombia = models.BooleanField(default=False)
    estados_unidos = models.BooleanField('Estados Unidos',default=False)
    bolivia = models.BooleanField(default=False)

    cfp= models.BooleanField(default=False)
    ramos_generales= models.BooleanField(default=False)
    investments= models.BooleanField(default=False)
    salud= models.BooleanField(default=False)
    vida= models.BooleanField(default=False)

    hispana_seguros = models.BooleanField(default=False)
    fpi = models.BooleanField(default=False)
    gi = models.BooleanField(default=False)
    bmiec_salud = models.BooleanField(default=False)
    cfp = models.BooleanField(default=False)
    mapfre = models.BooleanField(default=False)
    equinoccial = models.BooleanField(default=False)
    qbe = models.BooleanField(default=False)
    chubb = models.BooleanField(default=False)
    liberty = models.BooleanField(default=False)
    it = models.BooleanField(default=False)
    bupa = models.BooleanField(default=False)
    bmi_health = models.BooleanField(default=False)
    pc = models.BooleanField(default=False)
    paiic = models.BooleanField(default=False)
    nwl = models.BooleanField(default=False)
    bmi_life = models.BooleanField(default=False)
 


    class Meta:
        managed=True
        db_table = 'archivos'
        verbose_name = 'Biblioteca'

    def __unicode__(self):
        return self.nombre


class Poliza(models.Model):
    codigo = models.CharField(max_length=1000)
    agente=models.ForeignKey(Agente, models.DO_NOTHING, db_column='agente',related_name='polizas',blank=True, null=True)
    cliente=models.ForeignKey(Cliente, models.DO_NOTHING, db_column='cliente',blank=True, null=True)
    
    fecha_emision = models.DateField(blank=True, null=True)
    fecha = models.DateField(blank=True, default=datetime.datetime.today())
    #producto = models.ForeignKey(PropuestaCliente, models.DO_NOTHING, db_column='producto',blank=True, null=True)
    ramo_compania_producto = models.ForeignKey(RamoCompaniaProducto, models.DO_NOTHING, db_column='ramo_compania_producto', blank=True, null=True)
    
    numero_poliza = models.CharField(max_length=1000,blank=True, null=True)
    fecha_envio = models.DateField(blank=True, null=True)
    fecha_recibido = models.DateField(blank=True, null=True)
    fecha_aprobacion = models.DateField(blank=True, null=True)
    fecha_renovacion = models.DateField(blank=True, null=True)

    plan = models.CharField(max_length=1000,blank=True, null=True)
    anio_aporte = models.CharField(max_length=1000,blank=True, null=True)
    deducible = models.IntegerField(max_length=1000,blank=True, null=True)

    total = models.FloatField(max_length=1000,blank=True, null=True)
    comision = models.FloatField(max_length=1000,blank=True, null=True)
    prima = models.FloatField(max_length=1000,blank=True, null=True)
    forma_pago = models.CharField(max_length=1000,blank=True, null=True)


    class Meta:
        managed=True
        db_table = 'poliza'
        verbose_name = 'Poliza'

    def __unicode__(self):
        return self.codigo


class Datocomision(models.Model):
    producto = models.ForeignKey(RamoCompaniaProducto, blank=True, null=True,related_name='datocomision')
    rango_inicio = models.IntegerField('Inicio',blank=True, null=True)
    rango_fin = models.IntegerField('Fin',blank=True, null=True)
    pca_l1= models.FloatField('PCA L1',blank=True, null=True)
    pca_l2= models.FloatField('PCA L1',blank=True, null=True)
    senior_pca= models.FloatField('PCA Sr.',blank=True, null=True)
    relationship_manager= models.FloatField('RM',blank=True, null=True)
    relationship_manager_senior= models.FloatField('RM Sr.',blank=True, null=True)
    relationship_director= models.FloatField('RD',blank=True, null=True)
    bussiness_partner= models.FloatField('BP',blank=True, null=True)

    agente = models.ForeignKey(Agente, blank=True, null=True)
    #tipo_agente = models.ForeignKey(TipoAgente, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True, default=datetime.datetime.today())

    class Meta:
        managed=True
        verbose_name = 'Comision'

    def __unicode__(self):
        return str(self.rango_inicio)+'-'+str(self.rango_fin)+'   '+str(self.producto)



class Comision(models.Model):

    datocomision = models.ForeignKey(Datocomision, blank=True, null=True,related_name='comision')
    comision = models.CharField(max_length=1000)
    agente = models.ForeignKey(Agente, blank=True, null=True)
    tipo_agente = models.ForeignKey(TipoAgente, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True, default=datetime.datetime.today())

    class Meta:
        managed=True
        verbose_name = 'Comision/Agente'


