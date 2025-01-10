from django.db import models

class Campista(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=100)
    correo=models.CharField(max_length=100)
    telefono=models.CharField(max_length=10)
    direccion=models.TextField()

    def __str__(self):
        return f"{self.nombre} {self.correo} ({self.telefono})"

class Reservacion(models.Model):
    id=models.AutoField(primary_key=True)
    campista = models.ForeignKey(Campista, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    tipo_de_alojamiento = models.CharField(max_length=100)
    numero_de_personas = models.CharField(max_length=100)
    estado_de_la_reserva = models.CharField(max_length=100)
    observacion=models.TextField()
    def __str__(self):                      
        return f"{self.campista.nombre} - {self.estado_de_la_reserva}"


