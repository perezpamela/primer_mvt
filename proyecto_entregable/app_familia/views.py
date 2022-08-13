from django.http import HttpResponse
from app_familia.models import Familiar
from django.template import Template, loader

# Create your views here.
def getFamilia(self):
    familiares = Familiar.objects.values('nombre','apellido', 'fecha_nacimiento','cantidad_hijos','tiene_mascotas')
    familiares_dict= {
        'familiares':familiares
    }
    plantilla = loader.get_template('familia.html')
    documento = plantilla.render(familiares_dict)
    return HttpResponse(documento)

def insertFamilia(self, familiar):
    list_familiar = familiar.split('_')
    nvo_familiar = Familiar(
       nombre =list_familiar[0],
       apellido =list_familiar[1],
       fecha_nacimiento=list_familiar[2],
       cantidad_hijos=list_familiar[3],
       tiene_mascotas= list_familiar[4]
    )
    nvo_familiar.save()
    return HttpResponse(f'El familiar: {nvo_familiar.nombre} {nvo_familiar.apellido} se guardó correctamente.')
       
