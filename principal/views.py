# encoding: utf-8

from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.core.mail import EmailMessage
from django.shortcuts import render_to_response, get_object_or_404, render
from django.contrib.auth.forms import UserCreationForm

from principal.models import Cliente, Aseguradora, Siniestro, Factura, Profesional, Nota, Asignado, Documentacion
# noinspection PyPep8
from principal.forms import Clienteform, Siniestroform, Agenteform, Aseguradoraform, Tramitadorciaform, Profesionalform, \
	Facturaform, Documentacionform, Notaform
# Create your views here.
# noinspection PyPep8
def inicio (request):
	clientes = Cliente.objects.all ()
	return render_to_response ('listado_clientes.html', {'lista': clientes}, context_instance=RequestContext (request))


# muestra la lista de clientes en la plantilla
# noinspection PyPep8
def lista_clientes (request):
	clientes = Cliente.objects.all ()
	return render_to_response ('listado_clientes.html', {'lista': clientes}, context_instance=RequestContext (request))


# detalle de los clientes
def cliente_detalle (request, cliente_id):
	dato = get_object_or_404 (Cliente, pk=cliente_id)
	siniestros = Siniestro.objects.filter (cliente=dato)
	return render_to_response ('detalle_cliente.html', {'cliente': dato, 'siniestros': siniestros},
	                           context_instance=RequestContext (request))


def siniestro_detalle (request, siniestro_id):
	dato = get_object_or_404 (Siniestro, pk=siniestro_id)
	# cliente= Cliente.objects.filter (id=dato)
	facturas = Factura.objects.filter (siniestro=dato)
	notas = Nota.objects.filter (siniestro=dato)
	documentacion = Documentacion.objects.filter (siniestro=dato)
	asignado = Asignado.objects.filter (siniestro=dato)

	return render_to_response ('detalle_siniestro.html',
	                           {'siniestro': dato, 'cliente': cliente, 'facturas': facturas, 'notas': notas,
	                            'documentacion': documentacion, 'asignado': asignado},
	                           context_instance=RequestContext (request))


# Muestra el formulario,lo valida y si el formulario se ha rellenado completamente lo guarda en la base de datos
# clientes
def nuevo_cliente (request):
	if request.method == 'POST':
		formulario = Clienteform (request.POST)
		if formulario.is_valid ():
			formulario.save ()
			return HttpResponseRedirect ('/')
	else:
		formulario = Clienteform ()
	return render_to_response ('nuevo.html', {'formulario': formulario}, context_instance=RequestContext (request))


# agentes
def nuevo_agente (request):
	if request.method == 'POST':
		formulario = Agenteform (request.POST)
		if formulario.is_valid ():
			formulario.save ()
			return HttpResponseRedirect ('/')
	else:
		formulario = Agenteform ()
	return render_to_response ('nuevo.html', {'formulario': formulario}, context_instance=RequestContext (request))


# obtiene la id del cliente de la barra de direcciones y lo introduce en la base de datos cuando se guarda un siniestro
def nuevo_siniestro (request, cliente_id):
	dato = get_object_or_404 (Cliente, pk=cliente_id)
	if request.method == 'POST':
		formulario = Siniestroform (request.POST)
		if formulario.is_valid ():
			siniestros = formulario.save (commit=False)
			siniestros.cliente = dato
			siniestros.save ()
			return HttpResponseRedirect ('/')
	else:
		formulario = Siniestroform ()
	return render_to_response ('nuevo.html', {'formulario': formulario}, context_instance=RequestContext (request))


# aseguradora
def nueva_aseguradora (request):
	if request.method == 'POST':
		formulario = Aseguradoraform (request.POST)
		if formulario.is_valid ():
			formulario.save ()
			return HttpResponseRedirect ('/')
	else:
		formulario = Aseguradoraform ()
	return render_to_response ('nuevo.html', {'formulario': formulario}, context_instance=RequestContext (request))


# tramitador cia
def nuevo_tramitadorcia (request, aseguradora_id):
	dato = get_object_or_404 (Aseguradora, pk=aseguradora_id)
	if request.method == 'POST':
		formulario = Tramitadorciaform (request.POST)
		if formulario.is_valid ():
			tracia = formulario.save (commit=False)
			tracia.aseguradora = dato
			tracia.save ()
			return HttpResponseRedirect ('/')
	else:
		formulario = Tramitadorciaform ()
	return render_to_response ('nuevo.html', {'formulario': formulario}, context_instance=RequestContext (request))


# profesional
def nuevo_profesional (request):
	if request.method == 'POST':
		formulario = Profesionalform (request.POST)
		if formulario.is_valid ():
			formulario.save ()
			return HttpResponseRedirect ('/')
	else:
		formulario = Profesionalform ()
	return render_to_response ('nuevo.html', {'formulario': formulario}, context_instance=RequestContext (request))


# factura
def nueva_factura (request):
	if request.method == 'POST':
		formulario = Facturaform (request.POST)
		if formulario.is_valid ():
			formulario.save ()
			return HttpResponseRedirect ('/')
	else:
		formulario = Facturaform ()
	return render_to_response ('nuevo.html', {'formulario': formulario}, context_instance=RequestContext (request))


# documentacion
def nueva_documentacion (request):
	if request.method == 'POST':
		formulario = Documentacionform (request.POST)
		if formulario.is_valid ():
			formulario.save ()
			return HttpResponseRedirect ('/')
	else:
		formulario = Documentacionform ()
	return render_to_response ('nuevo.html', {'formulario': formulario}, context_instance=RequestContext (request))


# notas
def nueva_nota (request):
	if request.method == 'POST':
		formulario = Notaform (request.POST)
		if formulario.is_valid ():
			formulario.save ()
			return HttpResponseRedirect ('/')
	else:
		formulario = Notaform ()
	return render_to_response ('nuevo.html', {'formulario': formulario}, context_instance=RequestContext (request))

