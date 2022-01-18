from django.shortcuts import render #, redirect
from core.models import Evento

# Create your views here.


#def index(request):
#    return redirect('/agenda/')


def lista_eventos(request):
    #usuario = request.user
    #evento = Evento.objects.filter(usuario=usuario)    #filtrar pelo user logado
    #return render(request, 'agenda.html')
    #evento = Evento.objects.get(pk=2)
    evento = Evento.objects.all()
    dados = {'eventos': evento}
    #response = {'evento': evento}
    #return render(request, 'agenda.html', response)
    return render(request, 'agenda.html', dados)

