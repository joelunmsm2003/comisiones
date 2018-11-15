from django.contrib.auth.models import User
from app.models import *
from rest_framework import serializers


class PolizaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poliza
        fields = ('id', 'numero_poliza', 'fecha')

class AgentejerarquiaSerializer(serializers.ModelSerializer):
    
	country_manager=serializers.StringRelatedField(many=False)
	bussiness_partner=serializers.StringRelatedField(many=False)
	relation_ship_director=serializers.StringRelatedField(many=False)
	relation_management=serializers.StringRelatedField(many=False)
	relation_management_senior=serializers.StringRelatedField(many=False)
	private_client=serializers.StringRelatedField(many=False)
	private_client_senior=serializers.StringRelatedField(many=False)
	class Meta:
		model = Agentejerarquia
		fields = '__all__'


class DetalleagenteSerializer(serializers.ModelSerializer):

	tipo_agente = serializers.StringRelatedField(many=False, read_only=True)
	polizas = PolizaSerializer(many=True, read_only=True)
	agente_asigna = AgentejerarquiaSerializer(many=True, read_only=True)
	nivel = serializers.StringRelatedField(many=False, read_only=True)
	class Meta:
		model = Agente
		#fields = ('id', 'nombre','tipo_agente')
		fields = '__all__'

class AgenteSerializer(serializers.ModelSerializer):

	class Meta:
		model = Agente
		#fields = ('id', 'nombre','tipo_agente')
		fields = ('id','nombre')



