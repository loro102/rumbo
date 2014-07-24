# encoding: utf-8
from django.forms import ModelForm
from django import forms
from django.core.exceptions import ValidationError
from localflavor.es.forms import *
from localflavor.generic.forms import *

from principal.models import Cliente, Agente, Siniestro, Aseguradora, Tramitadorcia, Profesional, Factura, \
	Documentacion, Nota

# Formulario para introducir clientes
# noinspection PyPep8
class Clienteform (ModelForm):
	nif = ESIdentityCardNumberField (help_text='Introduzca el Dni,el Cif o el Nief')
	postal = ESPostalCodeField (help_text='Introduzca el código postal')
	ccc = ESCCCField (help_text='Introduzca la Cuenta Bancaria', required=False)

	class Meta:
		model = Cliente


# Formulario para introducir agentes
# noinspection PyPep8
class Agenteform (ModelForm):
	nif = ESIdentityCardNumberField (help_text='Introduzca el Dni,el Cif o el Nief')
	postal = ESPostalCodeField (help_text='Introduzca el código postal')
	ccc = ESCCCField (help_text='Introduzca la Cuenta Bancaria', required=False)

	class Meta:
		model = Agente


# Formulario para introducir siniestros
# noinspection PyPep8
class Siniestroform (ModelForm):
	reprenif = ESIdentityCardNumberField (help_text='Introduzca el Dni,el Cif o el Nief', required=False)

	class Meta:
		model = Siniestro
		exclude = ['cliente', 'fase', 'demanda', 'denuncia', 'juicio', 'audienciaprevia',
		           'ofertamotivada', 'respuestamotivada']
		widgets = dict (fechasiniestro=forms.DateInput (format='%d/%m/%y'),
		                horasiniestro=forms.TimeInput (format='%H:%m'),
		                fechabajalaboral=forms.DateInput (format='%d/%m/%y', attrs={'type': 'date'}),
		                fechaaltalaboral=forms.DateInput (format='%d/%m/%y', attrs={'type': 'date'}),
		                ingresohospitalario=forms.DateInput (format='%d/%m/%y', attrs={'type': 'date'}),
		                altahospitalaria=forms.DateInput (format='%d/%m/%y', attrs={'type': 'date'}),
		                altadireccion=forms.DateInput (format='%d/%m/%y', attrs={'type': 'date'}),
		                fechapoliza=forms.DateInput (format='%d/%m/%y', attrs={'type': 'date'}),
		                finpoliza=forms.DateInput (format='%d/%m/%y', attrs={'type': 'date'}),
		)


class Siniestrofullform (ModelForm):
	reprenif = ESIdentityCardNumberField (help_text='Introduzca el Dni,el Cif o el Nief', required=False)

	class Meta:
		model = Siniestro
		exclude = ['cliente']
		widgets = dict (fechasiniestro=forms.DateInput (format='%d/%m/%y'),
		                horasiniestro=forms.TimeInput (format='%H:%m'),
		                fechabajalaboral=forms.DateInput (format='%d/%m/%y'),
		                fechaaltalaboral=forms.DateInput (format='%d/%m/%y'),
		                ingresohospitalario=forms.DateInput (format='%d/%m/%y'),
		                altahospitalaria=forms.DateInput (format='%d/%m/%y'),
		                altadireccion=forms.DateInput (format='%d/%m/%y'),
		                fechapoliza=forms.DateInput (format='%d/%m/%y'),
		                finpoliza=forms.DateInput (format='%d/%m/%y'),
		)


# Formulario para introducir aseguradoras
class Aseguradoraform (ModelForm):
	class Meta:
		model = Aseguradora


# Formulario para introducir tramitadores de aseguradoras
class Tramitadorciaform (ModelForm):
	class Meta:
		model = Tramitadorcia
		exclude = ['aseguradora']


# Formulario para introducir profesionales
class Profesionalform (ModelForm):
	class Meta:
		model = Profesional


# Formulario para introducir documentacion
class Facturaform (ModelForm):
	class Meta:
		model = Factura


# Formulario para introducir facturas
class Documentacionform (ModelForm):
	class Meta:
		model = Documentacion

	# Formulario para introducir facturas


# Formulario para introducir notas
class Notaform (ModelForm):
	class Meta:
		model = Nota
