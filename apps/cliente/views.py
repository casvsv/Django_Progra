from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import FormularioCliente, FormularioModificarCliente, FormularioCuenta, FormularioModificarCuenta, FormularioTransaccion
from apps.modelo.models import Cliente, Cuenta, Transaccion
import random
from django.contrib import messages


def principal(request):
	lista=Cliente.objects.all().order_by('apellidos')
	listaCuentas=Cuenta.objects.all().order_by('numero')	
	context={
		'lista': lista,
		'listaCuentas': listaCuentas,
	}
	return render(request,'cliente/principal_cliente.html', context)



def crear(request):
	formulario = FormularioCliente(request.POST)
	formulariocuenta = FormularioCuenta(request.POST)
	usuario = request.user #Petición que es procesada por el framework y obtiene el usuario 
	if usuario.groups.filter(name = 'administrativo').exists():
		if request.method == 'POST':
			if formulario.is_valid() and formulariocuenta.is_valid():
				#Cliente
				datos=formulario.cleaned_data #Obtener todos los datos del formulario
				cliente=Cliente() #Crea un objeto de la case Cliente
				cliente.cedula=datos.get('cedula')
				cliente.nombres=datos.get('nombres')
				cliente.apellidos=datos.get('apellidos')
				cliente.genero=datos.get('genero')
				cliente.estado_civil=datos.get('estado_civil')
				cliente.fecha_nacimiento=datos.get('fecha_nacimiento')
				cliente.correo=datos.get('correo')
				cliente.telefono=datos.get('telefono')
				cliente.celular=datos.get('celular')
				cliente.direccion=datos.get('direccion')
				cliente.save()
				#Cuenta
				datoscuenta=formulariocuenta.cleaned_data #Obtener datos del formulario cuenta
				cuenta=Cuenta() #Crea un objeto de la clase Cuenta
				#
				Numero1=random.randrange(9999999, 99999999)
				Numero2=random.randrange(9999999, 99999999)
				Numero=Numero1*Numero2
				#
				cuenta.numero=Numero
				cuenta.estado=True
				cuenta.fechaApertura=datoscuenta.get('fechaApertura')
				cuenta.tipoCuenta=datoscuenta.get('tipoCuenta')
				cuenta.saldo=datoscuenta.get('saldo')
				cuenta.cliente=cliente
				cuenta.save()

				return redirect(principal)
	else:
		return render(request,'acceso_restringido.html')	
	context = {
		'f': formulario,
		'fc': formulariocuenta
	}
	return render(request, 'cliente/crear_cliente.html', context)


def modificar(request):
	dni = request.GET['cedula']
	cliente = Cliente.objects.get(cedula = dni)
	if request.method == 'POST':
		formulario=FormularioModificarCliente(request.POST)
		if formulario.is_valid():
			datos=formulario.cleaned_data
			cliente.nombres=datos.get('nombres')
			cliente.apellidos=datos.get('apellidos')
			cliente.genero=datos.get('genero')
			cliente.estado_civil=datos.get('estado_civil')
			cliente.fecha_nacimiento=datos.get('fecha_nacimiento')
			cliente.correo=datos.get('correo')
			cliente.telefono=datos.get('telefono')
			cliente.celular=datos.get('celular')
			cliente.direccion=datos.get('direccion')
			cliente.save()

			return redirect(principal)
	else:
		formulario=FormularioCliente(instance = cliente)
		context = {
			'dni': dni,
			'cliente': cliente,
			'formulario': formulario,
		}
		return render(request, 'cliente/modificar_cliente.html', context)


def modificar_cuenta(request):
	num = request.GET['numero']
	cuenta = Cuenta.objects.get(numero = num)
	if request.method == 'POST':
		formulario=FormularioModificarCuenta(request.POST)
		if formulario.is_valid():
			datos=formulario.cleaned_data
			cuenta.nombres=datos.get('tipoCuenta')
			cuenta.apellidos=datos.get('estado')
			cuenta.save()

			return redirect(principal)
	else:
		formulario=FormularioModificarCuenta(instance = cuenta)
		context = {
			'num': num,
			'cuenta': cuenta,
			'formulario': formulario,
		}
		return render(request, 'cliente/modificar_cuenta.html', context)		


def eliminar(request):
	dni = request.GET['cedula']
	cliente = Cliente.objects.get(cedula = dni)
	cliente.delete()
	return redirect(principal)


def eliminar_cuentas(request):
	num = request.GET['numero']
	cuenta = Cuenta.objects.get(numero = num)
	cuenta.delete()
	return redirect(principal)	


def cuentas(request):
	dni = request.GET['cedula']
	cliente = Cliente.objects.get(cedula = dni)
	listaCuentas=Cuenta.objects.filter(cliente_id=cliente.cliente_id).order_by('numero')	
	context={
		'listaCuentas': listaCuentas,
		'nombre_cliente': cliente.nombres + " " +cliente.apellidos,
		'ced': cliente.cedula
	}
	return render(request,'cliente/cuentas_cliente.html', context)


def crear_cuenta(request):
	dni = request.GET['cedula']
	cliente = Cliente.objects.get(cedula = dni)
	formulariocuenta = FormularioCuenta(request.POST)
	if request.method == 'POST':
		if formulariocuenta.is_valid():
			#Cuenta
			datoscuenta=formulariocuenta.cleaned_data #Obtener datos del formulario cuenta
			cuenta=Cuenta() #Crea un objeto de la clase Cuenta
			#
			Numero1=random.randrange(9999999, 99999999)
			Numero2=random.randrange(9999999, 99999999)
			Numero=Numero1*Numero2
			#
			cuenta.numero=Numero
			cuenta.estado=True
			cuenta.fechaApertura=datoscuenta.get('fechaApertura')
			cuenta.tipoCuenta=datoscuenta.get('tipoCuenta')
			cuenta.saldo=datoscuenta.get('saldo')
			cuenta.cliente=cliente
			cuenta.save()

			return redirect(principal)

	context = {
		'nombre_cliente': cliente.nombres + " " + cliente.apellidos,
		'fc': formulariocuenta,
	}
	return render(request, 'cliente/crear_cuenta.html', context)

def depositar(request):
	num = request.GET['numero']
	cuenta = Cuenta.objects.get(numero=num)
	cliente = Cliente.objects.get(cliente_id = cuenta.cliente_id)
	formulario = FormularioTransaccion(request.POST)
	if request.method == 'POST':
		if formulario.is_valid():
			datos = formulario.cleaned_data
			cuenta.saldo= cuenta.saldo + datos.get('valor')
			cuenta.save()
			transaccion = Transaccion()
			transaccion.tipo = 'deposito';
			transaccion.valor = datos.get('valor')
			transaccion.descripcion = datos.get('descripcion')
			transaccion.responsable = 'Yo pues quien mas'
			transaccion.cuenta = cuenta
			transaccion.save()
			deposito = float(datos.get('valor'))
			mensaje = 'Transacción Exitosa'
			return render (request, 'transaccion/status.html',locals())
	context = {
		'cliente': cliente.nombres + " " + cliente.apellidos,
		'cuenta': cuenta,
		'formulario': formulario,
	}
	return render(request, 'transaccion/depositar.html', context)

def retirar(request):
	num = request.GET['numero']
	cuenta = Cuenta.objects.get(numero=num)
	cliente = Cliente.objects.get(cliente_id = cuenta.cliente_id)
	formulario = FormularioTransaccion(request.POST)
	if request.method == 'POST':
		if formulario.is_valid():
			datos = formulario.cleaned_data
			if (datos.get('valor')<=cuenta.saldo):
				cuenta.saldo= cuenta.saldo - datos.get('valor')
				cuenta.save()
				transaccion = Transaccion()
				transaccion.tipo = 'deposito';
				transaccion.valor = datos.get('valor')
				transaccion.descripcion = datos.get('descripcion')
				transaccion.responsable = 'Yo pues quien mas'
				transaccion.cuenta = cuenta
				transaccion.save()
				deposito = float(datos.get('valor'))
				mensaje = 'Transacción Exitosa'
				return render (request, 'transaccion/status.html',locals())
			else:
				context = {
				'cliente': cliente.nombres + " " + cliente.apellidos,
				'cuenta': cuenta,
				'formulario': formulario,
				}
				messages.error(request, 'No cuenta con esa cantidad de dinero para poder retirar.')
				return render(request, 'transaccion/retirar.html', context)
	context = {
		'cliente': cliente.nombres + " " + cliente.apellidos,
		'cuenta': cuenta,
		'formulario': formulario,
	}
	return render(request, 'transaccion/retirar.html', context)

