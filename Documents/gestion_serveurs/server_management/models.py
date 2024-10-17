from django.db import models

# Create your models here.
from django.db import models

class Server(models.Model):
    server_name = models.CharField(max_length=100)
    server_ip = models.GenericIPAddressField()
    status = models.CharField(max_length=20, default="stopped")  # Statut
    cpu_usage = models.FloatField(default=0.0)  # Utilisation du CPU
    ram_usage = models.FloatField(default=0.0)  # Utilisation de la RAM

    def __str__(self):
        return self.server_name
