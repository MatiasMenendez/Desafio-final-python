from django.http import HttpResponse
from django.template import loader, Template, Context

def saludo(req):
    
    plantilla = loader.get_template('template.html')
    documento = plantilla.render()
    
    return HttpResponse(documento)