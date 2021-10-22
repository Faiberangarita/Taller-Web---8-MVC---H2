from django import template
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls.base import reverse

from .models import persona
from .forms import personaForm
def home(request):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context,request))


def index(request):
        personas = persona.objects.all()
        template = loader.get_template('persona/index.html')
        context ={
                'personas' : personas
        }

          
        
        return HttpResponse(template.render(context ,request))


def create_persona(request):
        if request.method == 'POST':
                form = personaForm(request.POST)

                if form.is_valid():
                        nombre = form.cleaned_data ['nombre']
                        documento = form.cleaned_data ['documento']
                        personac = persona(nombre = nombre , documento = documento)
                        personac.save()
                        return HttpResponseRedirect(reverse('index'))



        else:
                form = personaForm()

        return render(request,'persona/create_persona.html' , {'form' : form})
        

# Create your views here.
