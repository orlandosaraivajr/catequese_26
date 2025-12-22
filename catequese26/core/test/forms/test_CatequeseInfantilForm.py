import datetime
from django.test import TestCase
from core.models import CatequeseInfantilModel
from core.forms import CatequeseInfantilForm
from django.utils import timezone



class CatequeseInfantilFormHorarioTests(TestCase):

    def setUp(self):
        self.valid_base_data = {
            'nome': 'Maria Silva',
            'sexo': 'F',
            'data_nascimento': datetime.date(2018, 5, 10),
            'naturalidade': 'São Paulo',

            'nome_pai': 'João da Silva',
            'nome_mae': 'Ana da Silva',

            'endereco': 'Rua teste',
            'cidade': 'SP',
            'uf': 'SP',

            'celular_pai': '1199999',
            'celular_mae': '1199999',

            'batizado': False,

            'horario': '1',  # será substituído a cada teste

            'possui_deficiencia': False,
            'possui_transtorno': False,
            'medicamento_uso_continuo': False,
            'acompanhamento_psicologico': False,

            'nome_responsavel': 'Maria Souza',
            'cpf_responsavel': '00011122233',
            'endereco_responsavel': 'Rua teste'
        }

    # ------------------------------------
    # helper
    # ------------------------------------
    def make_form(self, **kwargs):
        data = self.valid_base_data.copy()
        data.update(kwargs)
        return CatequeseInfantilForm(data=data)

    # ------------------------------------------------
    # PRE-CATEQUESE: idade projetada 6 a 8
    # horários permitidos = ['1','2','3','4']
    # ------------------------------------------------
    def test_pre_catequese_valido(self):
        """
        idade projetada 7 -> deve aceitar horário da lista pre-catequese
        """
        ano_atual = timezone.now().year + 1
        ano_nascimento = ano_atual - 7  # força idade 7
        form = self.make_form(
            data_nascimento=datetime.date(ano_nascimento, 1, 1),
            horario='2',
        )
        self.assertTrue(form.is_valid())

    def test_pre_catequese_invalido(self):
        """
        idade 7 não pode escolher horário que não seja 1 a 4
        """
        ano_atual = timezone.now().year + 1
        ano_nascimento = ano_atual - 7
        form = self.make_form(
            data_nascimento=datetime.date(ano_nascimento, 1, 1),
            horario='9',  # proibido
        )
        self.assertFalse(form.is_valid())
        self.assertIn("pré-catequese", form.errors.get("horario")[0])

    # ------------------------------------------------
    # CATEQUESE: idade projetada 9 a 11
    # horários permitidos = ['5','6','7','8','9']
    # ------------------------------------------------
    def test_catequese_valido(self):
        ano_atual = timezone.now().year + 1
        ano_nascimento = ano_atual - 10  # idade 10
        form = self.make_form(
            data_nascimento=datetime.date(ano_nascimento, 1, 1),
            horario='7'
        )
        self.assertTrue(form.is_valid())

    def test_catequese_invalido(self):
        ano_atual = timezone.now().year + 1
        ano_nascimento = ano_atual - 10
        form = self.make_form(
            data_nascimento=datetime.date(ano_nascimento, 1, 1),
            horario='3'  # inválido
        )
        self.assertFalse(form.is_valid())
        self.assertIn("catequese.", form.errors.get("horario")[0])

    # ------------------------------------------------
    # 12+
    # horários permitidos = ['10','11']
    # ------------------------------------------------
    def test_12mais_valido(self):
        ano_atual = timezone.now().year + 1
        ano_nascimento = ano_atual - 12  # idade 12
        form = self.make_form(
            data_nascimento=datetime.date(ano_nascimento, 1, 1),
            horario='10'
        )
        self.assertTrue(form.is_valid())

    def test_12mais_invalido(self):
        ano_atual = timezone.now().year + 1
        ano_nascimento = ano_atual - 13  # idade 13
        form = self.make_form(
            data_nascimento=datetime.date(ano_nascimento, 1, 1),
            horario='5'
        )
        self.assertFalse(form.is_valid())
        self.assertIn("catequese 12+", form.errors.get("horario")[0])

    # ------------------------------------------------
    # Adulto (idade >= 14)
    # ------------------------------------------------
    def test_horario_adulto(self):
        ano_atual = timezone.now().year + 1
        ano_nascimento = ano_atual - 16
        form = self.make_form(
            data_nascimento=datetime.date(ano_nascimento, 1, 1),
            horario='11'
        )
        self.assertFalse(form.is_valid())
        self.assertIn("adulto", form.errors.get("horario")[0])


class CatequeseInfantilFormLimiteHorarioTests(TestCase):

    def setUp(self):
        self.base_data = {
            'nome': 'Maria Silva',
            'sexo': 'F',
            'data_nascimento': datetime.date(2018, 5, 10),
            'naturalidade': 'São Paulo',

            'nome_pai': 'João da Silva',
            'nome_mae': 'Ana da Silva',

            'endereco': 'Rua teste',
            'cidade': 'SP',
            'uf': 'SP',

            'celular_pai': '1199999',
            'celular_mae': '1199999',

            'batizado': False,

            'horario': '1',  # horário alvo do teste

            'possui_deficiencia': False,
            'possui_transtorno': False,
            'medicamento_uso_continuo': False,
            'acompanhamento_psicologico': False,

            'nome_responsavel': 'Maria Souza',
            'cpf_responsavel': '00011122233',
            'endereco_responsavel': 'Rua teste'
        }

    # helper
    def make_form(self, **kwargs):
        data = self.base_data.copy()
        data.update(kwargs)
        return CatequeseInfantilForm(data=data)

    def test_limite_20_por_horario_valido(self):
        """
        Deve aceitar cadastro quando ainda houver menos de 20 registros
        no mesmo horário
        """
        for i in range(19):
            CatequeseInfantilModel.objects.create(
                nome=f"Crianca {i}",
                sexo='F',
                data_nascimento=datetime.date(2018, 1, 1),
                naturalidade='SP',
                horario='1'
            )

        form = self.make_form(
            nome='Nova Criança',
            data_nascimento=datetime.date(2018, 2, 2),
            horario='1'
        )
        self.assertTrue(form.is_valid())

    def test_limite_20_por_horario_invalido(self):
        """
        Deve impedir o cadastro quando já existirem 20 registros
        no mesmo horário
        """
        for i in range(20):
            CatequeseInfantilModel.objects.create(
                nome=f"Crianca {i}",
                sexo='F',
                data_nascimento=datetime.date(2018, 1, 1),
                naturalidade='SP',
                horario='1'
            )

        form = self.make_form(
            nome='Crianca Excedente',
            data_nascimento=datetime.date(2018, 3, 3),
            horario='1'
        )

        self.assertFalse(form.is_valid())
        self.assertIn(
            "Limite de 20 catequizandos atingido",
            form.non_field_errors()[0]
        )
