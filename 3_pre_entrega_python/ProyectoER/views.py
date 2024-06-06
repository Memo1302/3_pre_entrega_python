from django.http import HttpResponse 
from django.template import Template, context           

def template(req):
    
   miHtml = open("/Users/Usuarios/Desktop/3_pre_entrega_python/ProyectoER/templates/template1.html") 
   
   plantilla = Template(miHtml.read())
   
   miHtml.close()
   
   miContexto = context()
   
   documento = plantilla.render(miContexto)
   
   return HttpResponse(documento)

