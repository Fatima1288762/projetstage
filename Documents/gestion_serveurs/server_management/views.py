from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Server

def list_servers(request):
    servers = Server.objects.all()
    return render(request, 'servers/list_servers.html', {'servers': servers})

def control_server(request, server_id):
    server = Server.objects.get(id=server_id)
    return render(request, 'servers/control_server.html', {'server': server})
