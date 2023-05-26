from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from agenda.models import lista_eventos

# Create your views here.
def index(request):
    return HttpResponse("Página View da Agenda ...")

def exibir_evento(request):
    evento = lista_eventos[1]
    name_template = "agenda/exibir_evento.html"
    # template = loader.get_template(name_template)
    # render_template = template.render(context={"evento": evento}, request=request)
    # return HttpResponse(render_template)
    return render(request=request, context={"evento": evento}, template_name=name_template)