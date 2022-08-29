from django.shortcuts import render
from models import familiares
from django.template import Context, Template, loader
from django.http import HttpResponse

# Create your views here.

def familiar(request):
  familiar1= familiares(nombre="Lorena", edad= 35, fecha_de_nacimiento="03-03-1987")
  familiar2= familiares(nombre="Mario", edad=61, fecha_de_nacimiento="17-07-1961")
  familiar3= familiares(nombre="Juana",edad=62, fecha_de_nacimiento="07-10-1960")

  familiar1.save()
  familiar2.save()
  familiar3.save()
  familiares={"nombre":familiar1.nombre,"edad":familiar1.edad,"fecha_de_nacimieto":familiar1.fecha_de_nacimiento,"nombre":familiar2.nombre,"edad":familiar2.edad,"fecha_de_nacimieto":familiar2.fecha_de_nacimiento,"nombre":familiar3.nombre,"edad":familiar3.edad,"fecha_de_nacimieto":familiar3.fecha_de_nacimiento,}
  plantillas=loader.get_template("template1.html")
  familiares=plantillas.render(familiares)
  
  return HttpResponse("familiares")