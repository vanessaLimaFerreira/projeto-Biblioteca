from django.db import models
from datetime import date


class Livros(models.Model):
    nome = models.CharField(max_length=100)
    autor = models.CharField(max_length=30)
    co_autor = models.CharField(max_length=50, blank=True)
    data_Cadastro = models.DateField(default = date.today)
    emprestado = models.BooleanField(default = False,null=True)
    nome_emprestado = models.CharField(max_length = 30, blank=True,null=True)
    data_emprestimo = models.DateTimeField(blank=True,null=True)
    data_devolucao = models.DateTimeField(blank=True,null=True)
    tempo_duracao = models.DateField(blank=True,null=True)

#configuração de classe para corrigir o nome da classe livross para livro
    class Meta:                      
        verbose_name = 'Livro'

    def __str__(self) :
        return self.nome