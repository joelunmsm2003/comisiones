from import_export import resources
from app.models import *

class AgenteResource(resources.ModelResource):
    class Meta:
        model = Agente