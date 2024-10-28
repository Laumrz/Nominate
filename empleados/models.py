from django.db import models
from datetime import date

# Definir una tupla con los valores del select genero_empleado
generos = (
    ("Masculino", "Masculino"),
    ("Femenino", "Femenino"),
    ("Otro", "Otro"),
)

tipoDocumento = (
    ('CC', 'Cédula de ciudadanía'),
    ('TI', 'Tarjeta de identidad'),
)

tipoEmpleado = (
    ('Dependiente', 'Dependiente'),
    ('Independiente', 'Independiente'),
)

nivelRiesgo = (
    ('Uno', 'Uno'),
    ('Dos', 'Dos'),
    ('Tres', 'Tres'),
    ('Cuatro', 'Cuatro'),
    ('Cinco', 'Cinco'),
)


class Empleado(models.Model):
    documento = models.IntegerField()
    tipo_documento = models.CharField(choices=tipoDocumento, max_length=100, default='CC') 
    fecha_nacimiento = models.DateField(default=date.today)
    nombre_empleado = models.CharField(max_length=200)
    apellido_empleado = models.CharField(max_length=100)
    email_empleado = models.EmailField(max_length=50)
    edad_empleado = models.IntegerField()
    genero_empleado = models.CharField(max_length=80, choices=generos)
    telefono_empleado = models.IntegerField(null=True, blank=True)
    nit_empresa = models.CharField(max_length=20, null=True, blank=True)
    fecha_contratacion = models.DateField(null=True, blank=True)
    tipo_empleado = models.CharField(choices=tipoEmpleado, max_length=200, null=True, blank=True)
    nivel_riesgo = models.CharField(choices=nivelRiesgo, max_length=200, null=True, blank=True)
    salario_empleado = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    foto_empleado = models.ImageField(
        upload_to='fotos_empleados/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def es_extension_valida(self):
        extensiones_validas = ['.jpg', '.jpeg', '.png', '.gif']
        return any(self.foto_empleado.name.lower().endswith(ext) for ext in extensiones_validas)

    """ la clase Meta dentro de un modelo se utiliza para proporcionar metadatos adicionales sobre el modelo."""
    class Meta:
        db_table = "empleados"
        ordering = ['-created_at']


class SeguridadSocial(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    salud = models.IntegerField(null=True, blank=True)
    pension = models.IntegerField(null=True, blank=True)
    caja_compensacion = models.IntegerField(null=True, blank=True)
    arl = models.IntegerField(null=True, blank=True)
    cesantias = models.IntegerField(null=True, blank=True)
    interes_cesantias = models.IntegerField(null=True, blank=True)
    prima = models.IntegerField(null=True, blank=True)
    fecha_actual = models.DateField()

    def __str__(self):
        return f"Seguridad Social de {self.empleado.documento} - {self.fecha_actual}"