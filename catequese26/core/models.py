from django.db import models
from django.utils import timezone

class CatequeseInfantilModel(models.Model):
    SEXO_CHOICES = (
        ("M", "Masculino"),
        ("F", "Feminino"),
    )
    
    HORARIO_CATEQUESE = (
        ("1", "Pré-Catequese - Segunda às 19:30h"),
        ("2", "Pré-Catequese - Terça às 19:30h"),
        ("3", "Pré-Catequese - Sábado às 09h"),
        ("4", "Pré-Catequese - Sábado às 10:30h"),
        ("5", "1a Etapa - Segunda às 19:30h"),
        ("6", "1a Etapa - Terça às 19:30h"),
        ("7", "1a Etapa - Quarta às 19:30h"),
        ("8", "1a Etapa - Sábado às 09h"),
        ("9", "1a Etapa - Sábado às 10:30h"),
        ("10", "12+ - Terça às 19:30h"),
        ("11", "12+ - Quinta ás 19:30h"),
    )

    nome = models.CharField(max_length=150)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    data_nascimento = models.DateField()
    naturalidade = models.CharField(max_length=100, blank=True, null=True)

    nome_pai = models.CharField(max_length=150, default='')
    nome_mae = models.CharField(max_length=150, default='')

    endereco = models.CharField(max_length=255)
    cidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)

    celular_pai = models.CharField(max_length=20, default='')
    celular_mae = models.CharField(max_length=20, default='')

    batizado = models.BooleanField(default=False)
    batizado_data = models.DateField(blank=True, null=True)
    batizado_diocese = models.CharField(max_length=150, blank=True, null=True)
    batizado_paroquia = models.CharField(max_length=150, blank=True, null=True)
    batizado_celebrante = models.CharField(max_length=150, blank=True, null=True)
    
    horario = models.CharField(max_length=2, choices=HORARIO_CATEQUESE)
    
    possui_deficiencia = models.BooleanField(default=False)
    descricao_deficiencia = models.TextField(blank=True, null=True)
    
    possui_transtorno = models.BooleanField(default=False)
    descricao_transtorno = models.TextField(blank=True, null=True)
    
    medicamento_uso_continuo = models.BooleanField(default=False)
    descricao_medicamento = models.TextField(blank=True, null=True)
    medicamento_horario = models.CharField(max_length=100, blank=True, null=True)
    
    acompanhamento_psicologico = models.BooleanField(default=False)
    descricao_acompanhamento = models.TextField(blank=True, null=True)
    
    # Termo de uso de Imagem
    
    nome_responsavel = models.CharField(max_length=150)
    cpf_responsavel = models.CharField(max_length=14)
    endereco_responsavel = models.CharField(max_length=255)
    
    # Ficha Impressa
    ficha_impressa = models.BooleanField(default=False)
    ficha_assinada = models.BooleanField(default=False)

    criado_em = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nome


class CrismaModel(models.Model):
    SEXO_CHOICES = (
        ("M", "Masculino"),
        ("F", "Feminino"),
    )
    HORARIO_CRISMA = (
        ("1", "Quinta às 19:30h"),
        ("2", "Sábado às 09h"),
        ("3", "Sábado às 10:30h"),
    )
    
    nome = models.CharField(max_length=150)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    data_nascimento = models.DateField()
    naturalidade = models.CharField(max_length=100, blank=True, null=True)

    nome_pai = models.CharField(max_length=150, default='')
    nome_mae = models.CharField(max_length=150, default='')

    endereco = models.CharField(max_length=255)
    cidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)

    celular_pai = models.CharField(max_length=20, default='')
    celular_mae = models.CharField(max_length=20, default='')

    batizado = models.BooleanField(default=False)
    batizado_data = models.DateField(blank=True, null=True)
    batizado_diocese = models.CharField(max_length=150, blank=True, null=True)
    batizado_paroquia = models.CharField(max_length=150, blank=True, null=True)
    batizado_celebrante = models.CharField(max_length=150, blank=True, null=True)
    
    primeira_eucaristia = models.BooleanField(default=False)
    primeira_eucaristia_data = models.DateField(blank=True, null=True)
    primeira_eucaristia_diocese = models.CharField(max_length=150, blank=True, null=True)
    primeira_eucaristia_paroquia = models.CharField(max_length=150, blank=True, null=True)
    primeira_eucaristia_celebrante = models.CharField(max_length=150, blank=True, null=True)
   
    horario = models.CharField(max_length=2, choices=HORARIO_CRISMA)

    padrinho_nome = models.CharField(max_length=150, blank=True, null=True, default='')    
    padrinho_celular = models.CharField(max_length=20, blank=True, null=True, default='')
    
    # Termo de uso de Imagem
    
    nome_responsavel = models.CharField(max_length=150,default='')
    cpf_responsavel = models.CharField(max_length=14,default='')
    endereco_responsavel = models.CharField(max_length=255,default='')
    
    # Ficha Impressa
    ficha_impressa = models.BooleanField(default=False)
    ficha_assinada = models.BooleanField(default=False)
    
    criado_em = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nome


class Perseveranca_MEJ_Model(models.Model):
    SEXO_CHOICES = (
        ("M", "Masculino"),
        ("F", "Feminino"),
    )
    
    HORARIO_PERSEVERANCA = (
        ("1", "Perseverança - 11 a 14 anos - Quinta às 19:30h"),
        ("2", "MEJ - 15 a 25 anos - Quinta às 19:30h"),
    )

    nome = models.CharField(max_length=150)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    data_nascimento = models.DateField()
    naturalidade = models.CharField(max_length=100, blank=True, null=True)

    nome_pai = models.CharField(max_length=150, default='')
    nome_mae = models.CharField(max_length=150, default='')

    endereco = models.CharField(max_length=255)
    cidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)

    celular_pai = models.CharField(max_length=20, default='')
    celular_mae = models.CharField(max_length=20, default='')

    batizado = models.BooleanField(default=False)
    batizado_data = models.DateField(blank=True, null=True)
    batizado_diocese = models.CharField(max_length=150, blank=True, null=True)
    batizado_paroquia = models.CharField(max_length=150, blank=True, null=True)
    batizado_celebrante = models.CharField(max_length=150, blank=True, null=True)

    primeira_eucaristia = models.BooleanField(default=False)
    primeira_eucaristia_data = models.DateField(blank=True, null=True)
    primeira_eucaristia_diocese = models.CharField(max_length=150, blank=True, null=True)
    primeira_eucaristia_paroquia = models.CharField(max_length=150, blank=True, null=True)
    primeira_eucaristia_celebrante = models.CharField(max_length=150, blank=True, null=True)

    horario = models.CharField(max_length=2, choices=HORARIO_PERSEVERANCA)
    
    possui_deficiencia = models.BooleanField(default=False)
    descricao_deficiencia = models.TextField(blank=True, null=True)
    
    possui_transtorno = models.BooleanField(default=False)
    descricao_transtorno = models.TextField(blank=True, null=True)
    
    medicamento_uso_continuo = models.BooleanField(default=False)
    descricao_medicamento = models.TextField(blank=True, null=True)
    medicamento_horario = models.CharField(max_length=100, blank=True, null=True)
    
    acompanhamento_psicologico = models.BooleanField(default=False)
    descricao_acompanhamento = models.TextField(blank=True, null=True)
    
    # Termo de uso de Imagem
    
    nome_responsavel = models.CharField(max_length=150)
    cpf_responsavel = models.CharField(max_length=14)
    endereco_responsavel = models.CharField(max_length=255)
    
    # Ficha Impressa
    ficha_impressa = models.BooleanField(default=False)
    ficha_assinada = models.BooleanField(default=False)

    criado_em = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.nome


class CatequeseAdultoModel(models.Model):
    SEXO_CHOICES = (
        ("M", "Masculino"),
        ("F", "Feminino"),
    )
    HORARIO_CATEQUESE_ADULTO = (
        ("1", "Terça às 19:30h"),
        ("2", "Sábado às 08h"),
    )
    
    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=14,default='')
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    celular = models.CharField(max_length=20, default='')
    data_nascimento = models.DateField()
    naturalidade = models.CharField(max_length=100, blank=True, null=True)

    nome_pai = models.CharField(max_length=150, default='')
    nome_mae = models.CharField(max_length=150, default='')

    endereco = models.CharField(max_length=255)
    cidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)
    estado_civil = models.CharField(max_length=50)

    batizado = models.BooleanField(default=False)
    batizado_data = models.DateField(blank=True, null=True)
    batizado_diocese = models.CharField(max_length=150, blank=True, null=True)
    batizado_paroquia = models.CharField(max_length=150, blank=True, null=True)
    batizado_celebrante = models.CharField(max_length=150, blank=True, null=True)
    
    primeira_eucaristia = models.BooleanField(default=False)
    primeira_eucaristia_data = models.DateField(blank=True, null=True)
    primeira_eucaristia_diocese = models.CharField(max_length=150, blank=True, null=True)
    primeira_eucaristia_paroquia = models.CharField(max_length=150, blank=True, null=True)
    primeira_eucaristia_celebrante = models.CharField(max_length=150, blank=True, null=True)

    casado_igreja = models.BooleanField(default=False)
    casado_igreja_data = models.DateField(blank=True, null=True)
    casado_igreja_diocese = models.CharField(max_length=150, blank=True, null=True)
    casado_igreja_paroquia = models.CharField(max_length=150, blank=True, null=True)
    casado_igreja_celebrante = models.CharField(max_length=150, blank=True, null=True)

    horario = models.CharField(max_length=2, choices=HORARIO_CATEQUESE_ADULTO)

    padrinho_nome = models.CharField(max_length=150, blank=True, null=True, default='')    
    padrinho_celular = models.CharField(max_length=20, blank=True, null=True, default='')
    
    # Ficha Impressa
    ficha_impressa = models.BooleanField(default=False)
    ficha_assinada = models.BooleanField(default=False)

    criado_em = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nome