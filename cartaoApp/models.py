from django.db import models

class Validar(models.Model):
    id_validar = models.AutoField(primary_key=True)
    cartao_validar =models.CharField(max_length=255 ,null=False)
    cpf_validar =models.CharField(max_length=255 ,null=False)
    nome_validar =models.CharField(max_length=255 ,null=False)
    codigo_validar =models.CharField(max_length=255 ,null=False)
    data_validar =models.CharField(max_length=255 ,null=False)

    def __str__(self):
        return self.nome_validar
