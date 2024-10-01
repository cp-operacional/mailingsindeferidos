from django.db import models

class Estados(models.Model):
    codigo_uf = models.IntegerField(null=True)
    uf = models.CharField(max_length=2, null=True)
    nome = models.CharField(max_length=100, null=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    regiao = models.CharField(max_length=50, null=True)

    class Meta:
        db_table = 'estados_ibge'

class Municipios(models.Model):
    codigo_ibge = models.IntegerField(null=True)
    nome = models.CharField(max_length=255, null=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    capital = models.IntegerField(null=True)
    codigo_uf = models.IntegerField(null=True)
    siafi_id = models.IntegerField(null=True)
    ddd = models.IntegerField(null=True)
    fuso_horario = models.CharField(max_length=50, null=True)

    class Meta:
        db_table = 'municipios_ibge'
