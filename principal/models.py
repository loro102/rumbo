#encoding: utf-8
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.exceptions import ValidationError

# Create your models here.
#Datos que se van a introducir del agente
class agente (models.Model):
	id= models.AutoField(unique=True,primary_key=True)
	nombre= models.CharField(max_length=255)
	nif=models.CharField(max_length=100,null=True, blank=True)
	direccion=models.CharField(max_length=255)
	postal=models.CharField(max_length=5)
	localidad=models.CharField(max_length=255)
	provincia=models.CharField(max_length=50)
	profesion=models.CharField(max_length=50)
	contrato=models.DateField(verbose_name='Fecha de Contrato',null=True, blank=True)
	telefono=models.CharField(max_length=9)
	telefono2=models.CharField(max_length=9,null=True, blank=True)
	mobil=models.CharField(max_length=9,null=True, blank=True)
	ccc=models.CharField(max_length=24,null=True, blank=True)
	comercial=models.CharField(max_length=255)
	placa=models.BooleanField(default='false', blank=True)
	pegatina=models.BooleanField(default='false', blank=True)
	activo=models.BooleanField(default='true', blank=True)
	notas=models.TextField(null=True, blank=True)

	def __str__(self):
		return  self.nombre


# Datos que se pide para introducir un cliente en la base de datos
@python_2_unicode_compatible
class cliente (models.Model):
	id = models.AutoField (unique=True, primary_key=True)
	nombre = models.CharField (max_length=255)
	apellido1 = models.CharField (max_length=255,verbose_name='Primer Apellido')
	apellido2 = models.CharField (max_length=255,verbose_name='Segundo Apellido')
	agente = models.ForeignKey(agente)
	nif = models.CharField (max_length=255,verbose_name='Nif o Dni')
	direccion = models.CharField (max_length=255)
	postal = models.CharField (max_length=5,verbose_name='Codigo Postal')
	localidad=models.CharField(max_length=255)
	provincia=models.CharField(max_length=50)
	telefono = models.CharField (max_length=9,null=True, blank=True)
	telefono2 = models.CharField (max_length=9,null=True, blank=True)
	mobil = models.CharField (max_length=9,null=True, blank=True)
	email = models.EmailField (max_length=75,verbose_name='Correo Electronico')
	ccc = models.CharField (max_length=24,verbose_name='Cuenta Bancaria')
	alta = models.DateField (auto_now=True)
	notas = models.TextField ()
	def __str__ (self):
		return u"%s   %s    %s" % (self.nombre, self.apellido1, self.apellido2)





#Datos para introducir profesionales
class profesional(models.Model):
	id=models.AutoField(unique=True,primary_key=True)
	tipo=models.CharField(max_length=50,verbose_name='Grupo Profesional')
	nombre=models.CharField(max_length=255)
	nif=models.CharField(max_length=50,null=True, blank=True)
	especialidad=models.CharField(max_length=100)
	direccion=models.CharField(max_length=255)
	postal=models.CharField(max_length=5,verbose_name='Código Postal')
	localidad=models.CharField(max_length=50)
	provincia=models.CharField(max_length=50)
	telefono=models.CharField(max_length=9,null=True, blank=True)
	telefono2=models.CharField(max_length=9,null=True, blank=True)
	telefono3=models.CharField(max_length=9,null=True, blank=True)
	fax=models.CharField(max_length=9,null=True, blank=True)
	email=models.EmailField(max_length=75,null=True, blank=True)
	pago=models.CharField(max_length=75,null=True, blank=True)
	indemnizacion=models.BooleanField(default='true', blank=True)

	def __str__(self):
		return self.nombre


#Datos para introducir siniestros
class siniestro (models.Model):
	id=models.AutoField(unique=True,primary_key=True)
	cliente=models.ForeignKey(cliente)
	representado=models.NullBooleanField()
	reprenombre=models.CharField(max_length=255,null=True, blank=True)
	reprenif=models.CharField(max_length=50,verbose_name ='Nif del representado',null=True, blank=True)
	tramitador=models.CharField(max_length=50,default='Rumbo Juridico')
	casotipo=models.CharField(max_length=50)
	casocont=models.CharField(max_length=50)
	fechaapertura=models.DateField(auto_now='now')
	fechasiniestro=models.DateField(verbose_name= 'Fecha del siniestro')
	horasiniestro=models.TimeField(verbose_name='Hora del siniestro')
	fechabajalaboral=models.DateField(verbose_name='Baja Laboral', null=True, blank=True)
	fechaaltalaboral=models.DateField(verbose_name='Alta Laboral',null=True, blank=True)
	ingresohospitalario=models.DateField(verbose_name='Ingreso Hospitalario', null=True, blank=True)
	altahospitalaria=models.DateField(verbose_name='Ingreso Hospitalario',null=True, blank=True)
	altadireccion=models.DateField(verbose_name='Alta Dirección Médica',null=True, blank=True)
	laboral=models.BooleanField(default=0,verbose_name='Accidente Laboral', blank=True)
	desarrollo=models.TextField(verbose_name='Desarrollo del Accidente', blank=True,max_length=15)
	lugar=models.CharField(max_length=50,verbose_name='Lugar del Accidente', blank=True)
	localidad=models.CharField(max_length=50,verbose_name='Localidad del Accidente', blank=True)
	descripcion=models.TextField(verbose_name='Descripción del Accidente', blank=True)
	condicion=models.CharField(max_length=50,null=True, blank=True)
	danovehiculo=models.TextField(verbose_name='Daños del Vehículo', null=True, blank=True)
	danopersonal=models.TextField(verbose_name='Daños Personales', null=True, blank=True)
	firmacarta=models.BooleanField(default=0,verbose_name='Firma carta de abogado procurador')
	asistencia=models.BooleanField(default=0,verbose_name='Asistencia Jurídica')
	cuantiaaj=models.CharField(max_length=10,verbose_name='Cuantía de Asistencia Jurídica',null=True , blank=True)
	vehiculo=models.CharField(max_length=100,verbose_name='Marca y modelo del Vehículo', blank=True)
	matricula=models.CharField(max_length=7,verbose_name='Matricula del Vehículo', blank=True)
	conductor=models.CharField(max_length=50,verbose_name='Conductor en el momento del accidente', blank=True)
	tomador=models.CharField(max_length=50,verbose_name='Tomador de la Póliza', blank=True)
	poliza=models.CharField(max_length=20,verbose_name='Nº de la Póliza de Seguro', blank=True)
	referencia=models.CharField(max_length=30,verbose_name='Nº de Referencia del Expediente',null=True, blank=True)
	compania=models.CharField(max_length=30,verbose_name='Compañía de seguros')
	fechapoliza=models.DateField(verbose_name='Fecha de la Póliza', blank=True)
	finpoliza=models.DateField(verbose_name='Fecha de Caducidad de la Póliza', blank=True)
	estimacion=models.CharField(max_length=10,verbose_name='Estimacíon de la indemnización',null=True, blank=True)

	def __str__ (self):
		return self.representado




