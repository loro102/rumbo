# encoding: utf-8
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


# Create your models here.
#Datos que se van a introducir del agente
class agente (models.Model):
	id = models.AutoField (unique=True, primary_key=True)
	nombre = models.CharField (max_length=255)
	nif = models.CharField (max_length=100, null=True, blank=True)
	direccion = models.CharField (max_length=255)
	postal = models.CharField (max_length=5)
	localidad = models.CharField (max_length=255)
	provincia = models.CharField (max_length=50)
	profesion = models.CharField (max_length=50)
	contrato = models.DateField (verbose_name='Fecha de Contrato', null=True, blank=True)
	telefono = models.CharField (max_length=9)
	telefono2 = models.CharField (max_length=9, null=True, blank=True)
	mobil = models.CharField (max_length=9, null=True, blank=True)
	ccc = models.CharField (max_length=24, null=True, blank=True)
	comercial = models.CharField (max_length=255)
	placa = models.BooleanField (default='false', blank=True)
	pegatina = models.BooleanField (default='false', blank=True)
	activo = models.BooleanField (default='true', blank=True)
	notas = models.TextField (null=True, blank=True)

	def __str__ (self):
		return self.nombre


# Datos que se pide para introducir aseguradoras
class aseguradora (models.Model):
	id = models.AutoField (unique=True, primary_key=True)
	aseguradora = models.CharField (max_length=255)
	telefono = models.CharField (max_length=9)
	fax = models.CharField (max_length=9, null=True, blank=True)
	email = models.EmailField (max_length=75)
	direccion = models.CharField (max_length=255)
	postal = models.CharField (max_length=255)
	localidad = models.CharField (max_length=255)
	provincia = models.CharField (max_length=255)
	notas = models.TextField ()

	def __str__ (self):
		return self.aseguradora


# Datos que se pide para introducir Tramitadores de la aseguradora
class tramitadorcia (models.Model):
	id = models.AutoField (unique=True, primary_key=True)
	nombre = models.CharField (max_length=255)
	telefono = models.CharField (max_length=9)
	fax = models.CharField (max_length=9, null=True, blank=True)
	email = models.EmailField (max_length=75)
	aseguradora = models.ForeignKey (aseguradora)
	cargo = models.CharField (max_length=255)
	notas = models.TextField ()

	def __str__ (self):
		return self.nombre


# Datos para introducir profesionales
class profesional (models.Model):
	id = models.AutoField (unique=True, primary_key=True)
	tipo = models.CharField (max_length=50, verbose_name='Grupo Profesional')
	nombre = models.CharField (max_length=255)
	nif = models.CharField (max_length=50, null=True, blank=True)
	especialidad = models.CharField (max_length=100)
	direccion = models.CharField (max_length=255)
	postal = models.CharField (max_length=5, verbose_name='Código Postal')
	localidad = models.CharField (max_length=50)
	provincia = models.CharField (max_length=50)
	telefono = models.CharField (max_length=9, null=True, blank=True)
	telefono2 = models.CharField (max_length=9, null=True, blank=True)
	telefono3 = models.CharField (max_length=9, null=True, blank=True)
	fax = models.CharField (max_length=9, null=True, blank=True)
	email = models.EmailField (max_length=75, null=True, blank=True)
	pago = models.CharField (max_length=75, null=True, blank=True)
	indemnizacion = models.BooleanField (default='true', blank=True)

	def __str__ (self):
		return self.nombre


# Datos que se pide para introducir un cliente en la base de datos
@python_2_unicode_compatible
class cliente (models.Model):
	id = models.AutoField (unique=True, primary_key=True)
	nombre = models.CharField (max_length=255)
	apellido1 = models.CharField (max_length=255, verbose_name='Primer Apellido')
	apellido2 = models.CharField (max_length=255, verbose_name='Segundo Apellido')
	agente = models.ForeignKey (agente)
	nif = models.CharField (max_length=255, verbose_name='Nif o Dni')
	direccion = models.CharField (max_length=255)
	postal = models.CharField (max_length=5, verbose_name='Codigo Postal')
	localidad = models.CharField (max_length=255)
	provincia = models.CharField (max_length=50)
	telefono = models.CharField (max_length=9, null=True, blank=True)
	telefono2 = models.CharField (max_length=9, null=True, blank=True)
	mobil = models.CharField (max_length=9, null=True, blank=True)
	email = models.EmailField (max_length=75, verbose_name='Correo Electronico')
	ccc = models.CharField (max_length=24, verbose_name='Cuenta Bancaria')
	alta = models.DateField (auto_now=True)
	notas = models.TextField ()

	def __str__ (self):
		return u"%s   %s    %s" % (self.nombre, self.apellido1, self.apellido2)





#Datos para introducir siniestros
class siniestro (models.Model):
	TIPO_CHOICES = (
	('1', '1'),
	('2', '2'),
	('3', '3'),
	('4', '4'),
	('5', '5'),
	)
	id = models.AutoField (unique=True, primary_key=True)
	cliente = models.ForeignKey (cliente)
	representado = models.BooleanField ()
	reprenombre = models.CharField (max_length=255, null=True, blank=True,
	                                verbose_name='Nombre y apellidos del representado')
	reprenif = models.CharField (max_length=50, verbose_name='Nif del representado', null=True, blank=True)
	tramitador = models.CharField (max_length=50, default='Rumbo Juridico')
	casotipo = models.CharField (max_length=50, choices=TIPO_CHOICES, default=1, verbose_name='caso tipo')
	casocont = models.CharField (max_length=50, choices=TIPO_CHOICES, default=1, verbose_name='caso tipo contable')
	fechaapertura = models.DateField (auto_now='now')
	fechasiniestro = models.DateField (verbose_name='Fecha del siniestro')
	horasiniestro = models.TimeField (verbose_name='Hora del siniestro')
	fechabajalaboral = models.DateField (verbose_name='Baja Laboral', null=True, blank=True)
	fechaaltalaboral = models.DateField (verbose_name='Alta Laboral', null=True, blank=True)
	ingresohospitalario = models.DateField (verbose_name='Ingreso Hospitalario', null=True, blank=True)
	altahospitalaria = models.DateField (verbose_name='Ingreso Hospitalario', null=True, blank=True)
	altadireccion = models.DateField (verbose_name='Alta Dirección Médica', null=True, blank=True)
	laboral = models.BooleanField (verbose_name='Accidente Laboral')
	desarrollo = models.TextField (verbose_name='Desarrollo del Accidente', blank=True, max_length=15)
	lugar = models.CharField (max_length=50, verbose_name='Lugar del Accidente', blank=True)
	localidad = models.CharField (max_length=50, verbose_name='Localidad del Accidente', blank=True)
	descripcion = models.TextField (verbose_name='Descripción del Accidente', blank=True)
	condicion = models.CharField (max_length=50, null=True, blank=True)
	danovehiculo = models.TextField (verbose_name='Daños del Vehículo', null=True, blank=True)
	danopersonal = models.TextField (verbose_name='Daños Personales', null=True, blank=True)
	firmacarta = models.BooleanField (verbose_name='Firma carta de abogado procurador')
	asistencia = models.BooleanField (verbose_name='Asistencia Jurídica')
	cuantiaaj = models.CharField (max_length=10, verbose_name='Cuantía de Asistencia Jurídica', null=True, blank=True)
	cuantiasanitaria = models.CharField (max_length=10, verbose_name='Cuantía de Asistencia Sanitaria', null=True,
	                                     blank=True)
	vehiculo = models.CharField (max_length=100, verbose_name='Marca y modelo del Vehículo', blank=True)
	matricula = models.CharField (max_length=7, verbose_name='Matricula del Vehículo', blank=True)
	conductor = models.CharField (max_length=50, verbose_name='Conductor en el momento del accidente', blank=True)
	tomador = models.CharField (max_length=50, verbose_name='Tomador de la Póliza', blank=True)
	poliza = models.CharField (max_length=20, verbose_name='Nº de la Póliza de Seguro', blank=True)
	referencia = models.CharField (max_length=30, verbose_name='Nº de Referencia del Expediente', null=True, blank=True)
	aseguradora = models.ForeignKey (aseguradora, verbose_name='Compañía de seguros')
	fechapoliza = models.DateField (verbose_name='Fecha de la Póliza', blank=True)
	finpoliza = models.DateField (verbose_name='Fecha de Caducidad de la Póliza', blank=True)
	estimacion = models.CharField (max_length=10, verbose_name='Estimacíon de la indemnización', null=True, blank=True)
	ofertamotivada = models.DateField (verbose_name='Fecha de Oferta Motivada', null=True, blank=True)
	audienciaprevia = models.DateField (verbose_name='Fecha de Audiencia Previa', null=True, blank=True)
	respuestamotivada = models.DateField (verbose_name='Fecha de Respuesta Motivada', null=True, blank=True)
	juicio = models.DateField (verbose_name='Fecha de Juicio', null=True, blank=True)
	denuncia = models.DateField (verbose_name='Fecha de Denuncia', null=True, blank=True)
	demanda = models.DateField (verbose_name='Fecha de Demanda', null=True, blank=True)
	tramitadorcia = models.ForeignKey (tramitadorcia, verbose_name='Tramitador de la Aseguradora', null=True,
	                                   blank=True)
	fase = models.CharField (max_length=255, verbose_name='Fase', null=True, blank=True)

	def __str__ (self):
		return self.reprenombre


# Datos que se pide para introducir facturas
class factura (models.Model):
	id = models.AutoField (unique=True, primary_key=True)
	siniestro = models.ForeignKey (siniestro)
	profesional = models.ForeignKey (profesional)
	numero = models.CharField (max_length=255)
	fecha = models.DateField ()
	descripcion = models.CharField (max_length=255)
	original = models.BooleanField ()
	totalfact = models.FloatField ()
	totalcli = models.FloatField ()
	totalemp = models.FloatField ()
	comision = models.BooleanField ()
	honorarios = models.BooleanField ()
	estadopago = models.CharField (max_length=255)
	estadocobro = models.CharField (max_length=255)
	estado = models.CharField (max_length=255)
	pagare = models.CharField (max_length=255)
	notas = models.TextField ()

	def __str__ (self):
		return self.numero


#Datos que se pide para introducir la documentacion del cliente
class documentacion (models.Model):
	id = models.AutoField (unique=True, primary_key=True)
	siniestro = models.ForeignKey (siniestro)
	entrada = models.DateField (auto_now=True)
	nombre = models.CharField (max_length=255)
	localizacion = models.CharField (max_length=255)
	salida = models.DateField ()
	archivo = models.CharField (max_length=255)

	def __str__ (self):
		return self.nombre


# Datos que se pide para introducir una nota
class nota (models.Model):
	id = models.AutoField (unique=True, primary_key=True)
	siniestro = models.ForeignKey (siniestro)
	escrito = models.DateField (auto_now=True)
	usuario = models.CharField (max_length=255)
	nota = models.TextField ()

	def __str__ (self):
		return self.nota



