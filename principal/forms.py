#encoding: utf-8
from django.forms import ModelForm
from django import forms
from django.core.exceptions import ValidationError
from localflavor.es.forms import *
from localflavor.generic.forms import *

from principal.models import cliente,agente,siniestro

#Formulario para introducir clientes
class clienteform(ModelForm):
	nif = ESIdentityCardNumberField ()
	postal = ESPostalCodeField ()
	ccc = ESCCCField ()
	class Meta:
		model = cliente


#Formulario para introducir agentes
class agenteform(ModelForm):
	nif = ESIdentityCardNumberField ()
	postal = ESPostalCodeField ()
	ccc = ESCCCField ()
	class Meta:
		model=agente


# Formulario para introducir siniestros
class siniestroform(ModelForm):
	reprenif = ESIdentityCardNumberField ()
	class Meta:
		model=siniestro
		exclude=['cliente']
		widgets = dict (fechasiniestro=forms.DateTimeInput (format='%d/%m/%y',attrs={'type':'date'}),
		                horasiniestro=forms.DateTimeInput (format='%H:%m',attrs={'type':'time'}),
		                fechabajalaboral=forms.DateInput(format='%d/%m/%y',attrs={'type':'date'}),
		                fechaaltalaboral=forms.DateInput(format='%d/%m/%y',attrs={'type':'date'}),
		                ingresohospitalario =forms.DateInput(format='%d/%m/%y',attrs={'type':'date'}),
		                altahospitalaria =forms.DateInput(format='%d/%m/%y',attrs={'type':'date'}),
		                altadireccion=forms.DateInput(format='%d/%m/%y',attrs={'type':'date'}),
		                fechapoliza=forms.DateInput(format='%d/%m/%y',attrs={'type':'date'}),
		                finpoliza =forms.DateInput(format='%d/%m/%y',attrs={'type':'date'}),

		)

