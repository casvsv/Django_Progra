from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.principal, name="cliente"),
	path('crear_cliente/', views.crear),
	path('modificar_cliente/', views.modificar),
	path('eliminar_cliente/', views.eliminar),
	path('cuentas_cliente/eliminar_cuenta/', views.eliminar_cuentas),
	path('cuentas_cliente/', views.cuentas),
	path('cuentas_cliente/modificar_cuenta/', views.modificar_cuenta),
	path('cuentas_cliente/crear_cuenta/', views.crear_cuenta),
	path('cuentas_cliente/deposito/', views.depositar),
	path('cuentas_cliente/retiro/', views.retirar),
]