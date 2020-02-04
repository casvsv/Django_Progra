from django.contrib import admin
from .models import Cliente
from .models import Cuenta
from .models import Transaccion

class AdminCliente(admin.ModelAdmin):
	list_display=["cedula","apellidos","nombres","genero"]
	list_editable=["apellidos","nombres"]
	list_filter=["genero","estado_civil"]
	search_fields=["cedula","apellidos","nombres"]	
	class Meta:
		mode=Cliente
admin.site.register(Cliente, AdminCliente)

class AdminCuenta(admin.ModelAdmin):
	list_display=["numero","estado","fechaApertura", "tipoCuenta", "cliente"]
	list_editable=["tipoCuenta","estado"]
	list_filter=["estado","fechaApertura", "tipoCuenta"]
	search_fields=["numero","cliente","fechaApertura", "tipoCuenta"]
	class Meta:
		mode=Cuenta
admin.site.register(Cuenta, AdminCuenta)

class AdminTransaccion(admin.ModelAdmin):
	list_display=["fecha","tipo","valor","responsable","cuenta"]
	list_filter=["tipo","fecha", "responsable"]
	search_fields=["tipo","fecha", "responsable"]
	class Meta:
		mode=Transaccion
admin.site.register(Transaccion, AdminTransaccion)

