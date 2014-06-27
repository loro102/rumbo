# encoding: utf-8

from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.core.mail import EmailMessage
from django.shortcuts import render_to_response, get_object_or_404,render
from django.contrib.auth.forms import UserCreationForm

from principal.models import cliente
from principal.forms import clienteform, siniestroform, agenteform





# Create your views here.
#muestra la lista de clientes en la plantilla
def lista_clientes (request):
	clientes = cliente.objects.all ()
	return render_to_response ('lista_clientes.html', {'lista': clientes})

#Muestra el formulario,lo valida y si el formulario se ha rellenado completamente lo guarda en la base de datos
# clientes
def nuevo_cliente (request):
	if request.method == 'POST':
		formulario = clienteform (request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect ('/')
	else:
		formulario = clienteform ()
	return render_to_response ('nuevo.html', {'formulario': formulario}, context_instance=RequestContext (request))


# agentes
def nuevo_agente (request):
	if request.method == 'POST':
		formulario = agenteform (request.POST)
		if formulario.is_valid ():
			formulario.save ()
			return HttpResponseRedirect ('/')
	else:
		formulario = agenteform ()
	return render_to_response ('nuevo.html', {'formulario': formulario}, context_instance=RequestContext (request))


#obtiene la id del cliente de la barra de direcciones y lo introduce en la base de datos cuando se guarda un siniestro
def nuevo_siniestro (request,cliente_id):
	dato = get_object_or_404(cliente, pk=cliente_id)
	if request.method == 'POST':
		formulario = siniestroform (request.POST)
		if formulario.is_valid():
			siniestro=formulario.save(commit=False)
			siniestro.cliente = dato
			siniestro.save()
			return HttpResponseRedirect ('/')
	else:
		formulario = siniestroform ()
	return render_to_response ('nuevo.html', {'formulario': formulario},
		                           context_instance=RequestContext (request))
