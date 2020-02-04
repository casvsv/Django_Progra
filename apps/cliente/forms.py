from django import forms
from apps.modelo.models import Cliente, Cuenta, Transaccion

class FormularioCliente(forms.ModelForm):
	class Meta: 
		model=Cliente
		fields=["cedula","nombres","apellidos","correo","fecha_nacimiento","estado_civil","genero","telefono","celular","direccion"]

class FormularioModificarCliente(forms.ModelForm):
	class Meta: 
		model=Cliente
		fields=["nombres","apellidos","correo","fecha_nacimiento","estado_civil","genero","telefono","celular","direccion"]



class FormularioCuenta(forms.ModelForm):
	class Meta: 
		model=Cuenta
		fields=["tipoCuenta","saldo"]		

class FormularioModificarCuenta(forms.ModelForm):
	class Meta: 
		model=Cuenta
		fields=["tipoCuenta","estado"]		


class FormularioTransaccion(forms.ModelForm):
	class Meta: 
		model=Transaccion
		fields=["valor","descripcion"]		