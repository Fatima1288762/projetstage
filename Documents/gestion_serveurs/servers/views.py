from django.shortcuts import render
from .models import Server  # Assurez-vous que ce modèle est bien importé

def list_servers(request):
    servers = Server.objects.all()  # Récupère tous les serveurs de la base de données
    return render(request, 'servers/list_servers.html', {'servers': servers})  # Assurez-vous que le chemin du template est correct
