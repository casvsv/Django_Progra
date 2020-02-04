from django.db import models

class Cliente(models.Model):
	listaGenero=(
		('f','Femenino'),
		('m','Masculino'),
	)
	listaEstado=(
		('soltero','Soltero'),
		('casado','Casado'),
		('divorciado','Divorciado'),
		('viudo','Viudo'),
	)

	cliente_id=models.AutoField(primary_key=True)
	cedula=models.CharField(max_length=10, unique=True, null=False)
	nombres=models.CharField(max_length=50, null=False)
	apellidos=models.CharField(max_length=50, null=False)
	direccion=models.TextField(max_length=50, default='Sin direccion')
	genero=models.CharField(max_length=15, choices=listaGenero, default='Femenino', null=False)
	estado_civil=models.CharField(max_length=15, choices=listaEstado, default='Soltero', null=False)
	fecha_nacimiento=models.DateField(auto_now=False, auto_now_add=False, null=False)
	correo=models.EmailField(max_length=50, null=False)
	celular=models.CharField(max_length=10)
	telefono=models.CharField(max_length=10)


class Cuenta(models.Model):
	listaTipo=(
		('corriente','Corriente'),
		('ahorros','Ahorro'),
	)

	cuenta_id=models.AutoField(primary_key=True)
	numero=models.CharField(max_length=20, unique=True, null=False)
	estado=models.BooleanField(default=True)
	fechaApertura=models.DateField(auto_now_add=True,null=False)
	tipoCuenta=models.CharField(max_length=30, choices=listaTipo, null=False,default='Ahorro')
	saldo=models.DecimalField(max_digits=10, decimal_places=3, null=False)
	cliente=models.ForeignKey(
		'Cliente',
		on_delete=models.CASCADE,
	)
	def _str_(self):
		string=str(self.saldo)+';'+str(self.cuenta_id)
		return string


class Transaccion(models.Model):
	listaTipoT=(
		('retiro','Retiro'),
		('deposito','Depósito'),
		('transferencia','Transferencia'),
	)
		
	transaccion_id=models.AutoField(primary_key=True)
	fecha=models.DateField(auto_now_add=True, null=False)
	tipo=models.CharField(max_length=30, choices=listaTipoT, null=False)
	valor=models.DecimalField(max_digits=10, decimal_places=3, null=False)
	descripcion=models.TextField(null=False)
	responsable=models.CharField(max_length=160, null=False)
	cuenta=models.ForeignKey(
		'Cuenta',
		on_delete=models.CASCADE,
	)
