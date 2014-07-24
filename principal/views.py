# encoding: utf-8

from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.core.mail import EmailMessage
from django.shortcuts import render_to_response, get_object_or_404, render
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Sum
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from principal.models import Cliente, Aseguradora, Siniestro, Factura, Profesional, Nota, Asignado, Documentacion, \
	Tramitadorcia, Agente
# noinspection PyPep8
from principal.forms import Clienteform, Siniestroform, Siniestrofullform, Agenteform, Aseguradoraform, \
	Tramitadorciaform, Profesionalform, \
	Facturaform, Documentacionform, Notaform
# Create your views here.

# Acceso a la aplicacion
def ingresar (request):
	if request.method == 'POST':
		formulario = AuthenticationForm (request.POST)
		if formulario.is_valid:
			usuario = request.POST ['username']
			clave = request.POST ['password']
			acceso = authenticate (username=usuario, password=clave)
			if acceso is not None:
				if acceso.is_active:
					login (request, acceso)
					return HttpResponseRedirect ('/principal')
				else:
					return render_to_response ('noactivo.html', context_instance=RequestContext (request))
			else:
				return render_to_response ('nousuario.html', context_instance=RequestContext (request))
		else:
			formulario = AuthenticationForm ()
			return render_to_response ('ingresar.html', {'formulario': formulario},
			                           context_instance=RequestContext (request))


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


def siniestro_detalle (request, siniestro_id, total1=0):
	dato = get_object_or_404 (Siniestro, pk=siniestro_id)
	client = dato.cliente_id
	cliente = Cliente.objects.get (id=dato.cliente_id)
	facturas = Factura.objects.filter (siniestro=dato)
	totalfacts1 = Factura.objects.filter (siniestro=dato, comision=0).aggregate (Sum ('totalfact'))
	totalfacts2 = Factura.objects.filter (siniestro=dato, comision=1).aggregate (Sum ('totalfact'))
	totalfactd1 = totalfacts1 ['totalfact__sum']
	totalfactd2 = totalfacts2 ['totalfact__sum']
	if totalfactd2 is None:
		totalfacto2 = 0
	else:
		totalfacto2 = totalfactd2 - (totalfactd2 * 0.21)

	if totalfactd1 is None:
		totalfacto1 = 0
	else:
		totalfacto1 = totalfactd1 + (totalfactd1 * 0.21)

	totalfactura = totalfacto1 + totalfacto2



	nota = Nota.objects.filter (siniestro=dato)
	documentacion = Documentacion.objects.filter (siniestro=dato)
	asignado = Asignado.objects.filter (siniestro=dato)

	return render_to_response ('detalle_siniestro.html',
	                           {'siniestro': dato, 'cliente': cliente, 'facturas': facturas, 'nota': nota,
	                            'documentacion': documentacion, 'asignado': asignado, 'totalfactura': totalfactura},
	                           context_instance=RequestContext (request))


# ############################################ Formularios ###########################################################
# Muestra el formulario,lo valida y si el formulario se ha rellenado completamente lo guarda en la base de datos
# clientes
def nuevo_cliente (request):
	titulo = 'Nuevo Cliente'
	if request.method == 'POST':
		formulario = Clienteform (request.POST)
		if formulario.is_valid ():
			formulario.save ()
			return HttpResponseRedirect ('/')
	else:
		formulario = Clienteform ()
	return render_to_response ('nuevo.html', {'formulario': formulario, 'titulo': titulo},
	                           context_instance=RequestContext (request))


def editar_cliente (request, cliente_id):
	titulo = 'Editar Cliente'
	dato = Cliente.objects.get (pk=cliente_id)
	if request.method == 'POST':
		formulario = Clienteform (request.POST, instance=dato)

		if formulario.is_valid ():
			# siniestros = formulario.save (commit=False)
			#siniestros.cliente = dato
			formulario.save ()
			return HttpResponseRedirect ('/')
	else:
		formulario = Clienteform (instance=dato)

	return render_to_response ('nuevo.html', {'formulario': formulario, 'titulo': titulo},
	                           context_instance=RequestContext (request))

# agentes
def nuevo_agente (request):
	titulo = 'Nuevo Agente'
	if request.method == 'POST':
		formulario = Agenteform (request.POST)
		if formulario.is_valid ():
			formulario.save ()
			return HttpResponseRedirect ('/')
	else:
		formulario = Agenteform ()
	return render_to_response ('nuevo.html', {'formulario': formulario, 'titulo': titulo},
	                           context_instance=RequestContext (request))


def editar_agente (request, agente_id):
	titulo = 'Editar Agente'
	dato = Agente.objects.get (pk=agente_id)
	if request.method == 'POST':
		formulario = Agenteform (request.POST, instance=dato)

		if formulario.is_valid ():
			# siniestros = formulario.save (commit=False)
			#siniestros.cliente = dato
			formulario.save ()
			return HttpResponseRedirect ('/')
	else:
		formulario = Agenteform (instance=dato)

	return render_to_response ('nuevo.html', {'formulario': formulario, 'titulo': titulo},
	                           context_instance=RequestContext (request))

# obtiene la id del cliente de la barra de direcciones y lo introduce en la base de datos cuando se guarda un siniestro
def nuevo_siniestro (request, cliente_id):
	titulo = 'Nuevo Siniestro'
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
	return render_to_response ('nuevo.html', {'formulario': formulario, 'titulo': titulo},
	                           context_instance=RequestContext (request))


def editar_siniestro (request, siniestro_id):
	titulo = 'Editar siniestro'
	dato = Siniestro.objects.get (pk=siniestro_id)
	cliente = Cliente.objects.get (id=dato.cliente_id)
	if request.method == 'POST':
		formulario = Siniestrofullform (request.POST, instance=dato)

		if formulario.is_valid ():
			# siniestros = formulario.save (commit=False)
			#siniestros.cliente = dato
			formulario.save ()
			return HttpResponseRedirect ('/')
	else:
		formulario = Siniestrofullform (instance=dato)

	return render_to_response ('nuevo.html', {'formulario': formulario, 'titulo': titulo, 'cliente': cliente},
	                           context_instance=RequestContext (request))
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


def editar_aseguradora (request, aseguradora_id):
	titulo = 'Editar Cliente'
	dato = Aseguradora.objects.get (pk=aseguradora_id)
	if request.method == 'POST':
		formulario = Aseguradoraform (request.POST, instance=dato)

		if formulario.is_valid ():
			# siniestros = formulario.save (commit=False)
			#siniestros.cliente = dato
			formulario.save ()
			return HttpResponseRedirect ('/')
	else:
		formulario = Aseguradoraform (instance=dato)

	return render_to_response ('nuevo.html', {'formulario': formulario, 'titulo': titulo},
	                           context_instance=RequestContext (request))


# tramitador cia
def nuevo_tramitadorcia (request, aseguradora_id):
	titulo = 'Nuevo Tramitador de la aseguradora'
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
	return render_to_response ('nuevo.html', {'formulario': formulario, 'titulo': titulo},
	                           context_instance=RequestContext (request))


def editar_tramitadorcia (request, tramitadorcia_id):
	titulo = 'Editar Tramitador'
	dato = Tramitadorcia.objects.get (pk=tramitadorcia_id)
	if request.method == 'POST':
		formulario = Tramitadorciaform (request.POST, instance=dato)

		if formulario.is_valid ():
			# siniestros = formulario.save (commit=False)
			#siniestros.cliente = dato
			formulario.save ()
			return HttpResponseRedirect ('/')
	else:
		formulario = Tramitadorciaform (instance=dato)

	return render_to_response ('nuevo.html', {'formulario': formulario, 'titulo': titulo},
	                           context_instance=RequestContext (request))

# profesional
def nuevo_profesional (request):
	titulo = 'Nuevo Profesional'
	if request.method == 'POST':
		formulario = Profesionalform (request.POST)
		if formulario.is_valid ():
			formulario.save ()
			return HttpResponseRedirect ('/')
	else:
		formulario = Profesionalform ()
	return render_to_response ('nuevo.html', {'formulario': formulario, 'titulo': titulo},
	                           context_instance=RequestContext (request))


def editar_profesional (request, profesional_id):
	titulo = 'Editar Cliente'
	dato = Profesional.objects.get (pk=profesional_id)
	if request.method == 'POST':
		formulario = Profesionalform (request.POST, instance=dato)

		if formulario.is_valid ():
			# siniestros = formulario.save (commit=False)
			#siniestros.cliente = dato
			formulario.save ()
			return HttpResponseRedirect ('/')
	else:
		formulario = Profesionalform (instance=dato)

	return render_to_response ('nuevo.html', {'formulario': formulario, 'titulo': titulo},
	                           context_instance=RequestContext (request))


# factura
def nueva_factura (request):
	titulo = 'Nueva Factura'
	if request.method == 'POST':
		formulario = Facturaform (request.POST)
		if formulario.is_valid ():
			formulario.save ()
			return HttpResponseRedirect ('/')
	else:
		formulario = Facturaform ()
	return render_to_response ('nuevo.html', {'formulario': formulario, 'titulo': titulo},
	                           context_instance=RequestContext (request))


# documentacion
def nueva_documentacion (request):
	titulo = 'Nueva Documentación'
	if request.method == 'POST':
		formulario = Documentacionform (request.POST)
		if formulario.is_valid ():
			formulario.save ()
			return HttpResponseRedirect ('/')
	else:
		formulario = Documentacionform ()
	return render_to_response ('nuevo.html', {'formulario': formulario, 'titulo': titulo},
	                           context_instance=RequestContext (request))


# notas
def nueva_nota (request):
	titulo = 'Nueva Nota'
	if request.method == 'POST':
		formulario = Notaform (request.POST)
		if formulario.is_valid ():
			formulario.save ()
			return HttpResponseRedirect ('/')
	else:
		formulario = Notaform ()
	return render_to_response ('nuevo.html', {'formulario': formulario, 'titulo': titulo},
	                           context_instance=RequestContext (request))

