# encoding: utf-8

from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.core.mail import EmailMessage
from django.shortcuts import render_to_response, get_object_or_404, render
from django.contrib.auth.forms import UserCreationForm

from principal.models import cliente, aseguradora
from principal.forms import clienteform, siniestroform, agenteform, aseguradoraform, tramitadorciaform, profesionalform, \
	facturaform, documentacionform, notaform





# Create your views here.
# muestra la lista de clientes en la plantilla
def lista_clientes (request):
	clientes = cliente.objects.all ()
	return render_to_response ('lista_clientes.html', {'lista': clientes})


#Muestra el formulario,lo valida y si el formulario se ha rellenado completamente lo guarda en la base de datos
# clientes
def nuevo_cliente (request):
	if request.method == 'POST':
		formulario = clienteform (request.POST)
		if formulario.is_valid ():
			formulario.save ()
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
def nuevo_siniestro (request, cliente_id):
	dato = get_object_or_404 (cliente, pk=cliente_id)
	if request.method == 'POST':
		formulario = siniestroform (request.POST)
		if formulario.is_valid ():
			siniestro = formulario.save (commit=False)
			siniestro.cliente = dato
			siniestro.save ()
			return HttpResponseRedirect ('/')
	else:
		formulario = siniestroform ()
	return render_to_response ('nuevo.html', {'formulario': formulario},
	                           context_instance=RequestContext (request))


# aseguradora
def nueva_aseguradora (request):
	if request.method == 'POST':
		formulario = aseguradoraform (request.POST)
		if formulario.is_valid ():
			formulario.save ()
			return HttpResponseRedirect ('/')
	else:
		formulario = aseguradoraform ()
	return render_to_response ('nuevo.html', {'formulario': formulario}, context_instance=RequestContext (request))


# tramitador cia
def nuevo_tramitadorcia (request, aseguradora_id):
	dato = get_object_or_404 (aseguradora, pk=aseguradora_id)
	if request.method == 'POST':
		formulario = tramitadorciaform (request.POST)
		if formulario.is_valid ():
			tramitadorcia = formulario.save (commit=False)
			tramitadorcia.aseguradora = dato
			tramitadorcia.save ()
			return HttpResponseRedirect ('/')
	else:
		formulario = tramitadorciaform ()
	return render_to_response ('nuevo.html', {'formulario': formulario}, context_instance=RequestContext (request))


# profesional
def nuevo_profesional (request):
	if request.method == 'POST':
		formulario = profesionalform (request.POST)
		if formulario.is_valid ():
			formulario.save ()
			return HttpResponseRedirect ('/')
	else:
		formulario = profesionalform ()
	return render_to_response ('nuevo.html', {'formulario': formulario}, context_instance=RequestContext (request))


# factura
def nueva_factura (request):
	if request.method == 'POST':
		formulario = facturaform (request.POST)
		if formulario.is_valid ():
			formulario.save ()
			return HttpResponseRedirect ('/')
	else:
		formulario = facturaform ()
	return render_to_response ('nuevo.html', {'formulario': formulario}, context_instance=RequestContext (request))


# documentacion
def nueva_documentacion (request):
	if request.method == 'POST':
		formulario = documentacionform (request.POST)
		if formulario.is_valid ():
			formulario.save ()
			return HttpResponseRedirect ('/')
	else:
		formulario = documentacionform ()
	return render_to_response ('nuevo.html', {'formulario': formulario}, context_instance=RequestContext (request))


# notas
def nueva_nota (request):
	if request.method == 'POST':
		formulario = notaform (request.POST)
		if formulario.is_valid ():
			formulario.save ()
			return HttpResponseRedirect ('/')
	else:
		formulario = notaform ()
	return render_to_response ('nuevo.html', {'formulario': formulario}, context_instance=RequestContext (request))

