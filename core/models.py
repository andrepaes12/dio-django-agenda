from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta

# Create your models here.
class Evento(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Título') #CharField = campo de input
    descricao = models.TextField(blank=True, null=True, verbose_name='Descrição') #TextField = Campo TextArea
    data_evento = models.DateTimeField(verbose_name='Data do Evento')    #DataTimeField = campo de data
    data_criacao = models.DateTimeField(auto_now=True, verbose_name='Data de Criação')
    local = models.CharField(blank=True, null=True, max_length=100, verbose_name='Localização')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário')

    #class Meta:
    #    db_table = 'evento'

    def __str__(self):
        return self.titulo

    def get_data_evento(self):
        return self.data_evento.strftime('%d/%m/%Y %H:%M h')

    def get_data_input_evento(self):
        return self.data_evento.strftime('%Y-%m-%dT%H:%M')

    def get_evento_atrasado(self):
        if self.data_evento < datetime.now():
            return True
        else:
            return False

    def get_evento_next(self):
        next_evento = datetime.now() + timedelta(hours=1)
        if self.data_evento < next_evento:
            return True
        else:
            return False

