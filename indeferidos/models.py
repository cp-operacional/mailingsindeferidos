from django.db import models

class Indeferidos(models.Model):
    cpf = models.BigIntegerField(null=True, blank=True)
    nome_completo = models.CharField(max_length=255, null=True, blank=True)
    data_nascimento = models.DateField(null=True, blank=True)
    data_indeferimento = models.DateField(null=True, blank=True)
    especie_beneficio = models.IntegerField(null=True, blank=True)
    descricao_especie_beneficio = models.CharField(max_length=255, null=True, blank=True)
    motivo_indeferimento = models.CharField(max_length=255, null=True, blank=True)
    sexo = models.CharField(max_length=20, null=True, blank=True)
    nome_mae = models.CharField(max_length=255, null=True, blank=True)
    endereco = models.TextField(null=True, blank=True)
    bairro = models.CharField(max_length=255, null=True, blank=True)
    cep = models.CharField(max_length=10, null=True, blank=True)
    municipio = models.CharField(max_length=255, null=True, blank=True)
    uf = models.CharField(max_length=2, null=True, blank=True)
    competencia_indeferimento = models.IntegerField(null=True, blank=True)
    ano_indeferimento = models.IntegerField(null=True, blank=True)
    clientela = models.CharField(max_length=255, null=True, blank=True)
    celular_1 = models.CharField(max_length=20, null=True, blank=True)
    resultado_celular_1 = models.TextField(null=True, blank=True)
    celular_2 = models.CharField(max_length=20, null=True, blank=True)
    resultado_celular_2 = models.TextField(null=True, blank=True)
    celular_3 = models.CharField(max_length=20, null=True, blank=True)
    resultado_celular_3 = models.TextField(null=True, blank=True)
    celular_4 = models.CharField(max_length=20, null=True, blank=True)
    resultado_celular_4 = models.TextField(null=True, blank=True)
    fixo_1 = models.CharField(max_length=20, null=True, blank=True)
    resultado_fixo_1 = models.TextField(null=True, blank=True)
    fixo_2 = models.CharField(max_length=20, null=True, blank=True)
    resultado_fixo_2 = models.TextField(null=True, blank=True)
    fixo_3 = models.CharField(max_length=20, null=True, blank=True)
    resultado_fixo_3 = models.TextField(null=True, blank=True)
    fixo_4 = models.CharField(max_length=20, null=True, blank=True)
    resultado_fixo_4 = models.TextField(null=True, blank=True)
    email_1 = models.EmailField(null=True, blank=True)
    email_2 = models.EmailField(null=True, blank=True)
    email_3 = models.EmailField(null=True, blank=True)
    email_4 = models.EmailField(null=True, blank=True)
    resultado_geral_contato = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'pf_indeferidos'

    def __str__(self):
        return f"{self.nome_completo} - CPF: {self.cpf}"

from django.db import models

class IndeferidosDone(models.Model):
    cpf = models.BigIntegerField(null=True, blank=True)

    class Meta:
        db_table = 'indeferidos_done'

    def __str__(self):
        return f"{self.nome_completo} - CPF: {self.cpf}"
