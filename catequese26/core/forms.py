from django import forms
from django.forms import ModelForm
from .models import CatequeseInfantilModel, CrismaModel


class CatequeseInfantilForm(ModelForm):
    class Meta:
        model = CatequeseInfantilModel
        fields = '__all__'
        exclude = ['ficha_impressa']

        labels = {
            'nome': 'Nome Completo:',
            'sexo': 'Sexo:',
            'data_nascimento': 'Data de Nascimento:',
            'naturalidade': 'Naturalidade:',

            'nome_pai': 'Nome do Pai:',
            'nome_mae': 'Nome da Mãe:',

            'endereco': 'Endereço:',
            'cidade': 'Cidade:',
            'uf': 'UF:',

            'celular_pai': 'Celular do Pai:',
            'celular_mae': 'Celular da Mãe:',

            'batizado': 'É Batizado?',
            'batizado_data': 'Data do Batismo:',
            'batizado_diocese': 'Diocese:',
            'batizado_paroquia': 'Paróquia:',
            'batizado_celebrante': 'Celebrante:',

            'horario': 'Horário da Catequese:',

            'possui_deficiencia': 'Possui Deficiência?',
            'descricao_deficiencia': 'Descrição da Deficiência:',

            'possui_transtorno': 'Possui Algum Transtorno?',
            'descricao_transtorno': 'Descrição do Transtorno:',

            'medicamento_uso_continuo': 'Toma Medicamento de Uso Contínuo?',
            'descricao_medicamento': 'Descrição do Medicamento:',
            'medicamento_horario': 'Horário do Medicamento:',

            'acompanhamento_psicologico': 'Faz Acompanhamento Psicológico?',
            'descricao_acompanhamento': 'Descrição do Acompanhamento:',

            'nome_responsavel': 'Nome do Responsável (para direito de imagem):',
            'cpf_responsavel': 'CPF do Responsável:',
            'endereco_responsavel': 'Endereço do Responsável:',
        }

        widgets = {

            # Dados principais
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o nome completo'}),
            'sexo': forms.Select(attrs={'class': 'form-select'}),
            'data_nascimento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'naturalidade': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cidade onde nasceu'}),

            # Filiação
            'nome_pai': forms.TextInput(attrs={'class': 'form-control'}),
            'nome_mae': forms.TextInput(attrs={'class': 'form-control'}),

            # Endereço
            'endereco': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Rua, número, bairro'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control'}),
            'uf': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 2, 'placeholder': 'Ex: SP'}),

            # Contatos
            'celular_pai': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(11) 99999-9999'}),
            'celular_mae': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(11) 99999-9999'}),

            # Batismo
            'batizado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'batizado_data': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'batizado_diocese': forms.TextInput(attrs={'class': 'form-control'}),
            'batizado_paroquia': forms.TextInput(attrs={'class': 'form-control'}),
            'batizado_celebrante': forms.TextInput(attrs={'class': 'form-control'}),

            # Horário Catequese
            'horario': forms.Select(attrs={'class': 'form-select'}),

            # Necessidades especiais
            'possui_deficiencia': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'descricao_deficiencia': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),

            'possui_transtorno': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'descricao_transtorno': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),

            # Medicamentos
            'medicamento_uso_continuo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'descricao_medicamento': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'medicamento_horario': forms.TextInput(attrs={'class': 'form-control'}),

            # Acompanhamento psicológico
            'acompanhamento_psicologico': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'descricao_acompanhamento': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),

            # Responsável
            'nome_responsavel': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf_responsavel': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '000.000.000-00'}),
            'endereco_responsavel': forms.TextInput(attrs={'class': 'form-control'}),
        }

        error_messages = {
            'nome': {'required': 'Informe o nome da criança.'},
            'data_nascimento': {'required': 'Informe a data de nascimento.'},
            'endereco': {'required': 'Informe o endereço.'},
            'cidade': {'required': 'Informe a cidade.'},
            'uf': {'required': 'Informe o estado (UF).'},
            'nome_responsavel': {'required': 'Informe o nome do responsável.'},
            'cpf_responsavel': {'required': 'Informe o CPF do responsável.'},
        }
        
    def clean(self):
        cleaned_data = super().clean()
        batizado = cleaned_data.get('batizado')

        if batizado:
            batizado_data = cleaned_data.get('batizado_data')
            batizado_diocese = cleaned_data.get('batizado_diocese')
            batizado_paroquia = cleaned_data.get('batizado_paroquia')
            batizado_celebrante = cleaned_data.get('batizado_celebrante')

            if not batizado_data:
                self.add_error('batizado_data', 'Informe a data do batismo.')
            if not batizado_diocese:
                self.add_error('batizado_diocese', 'Informe a diocese do batismo.')
            if not batizado_paroquia:
                self.add_error('batizado_paroquia', 'Informe a paróquia do batismo.')
            if not batizado_celebrante:
                self.add_error('batizado_celebrante', 'Informe o celebrante do batismo.')


class CrismaForm(ModelForm):
    class Meta:
        model = CrismaModel
        fields = '__all__'
        exclude = ['ficha_impressa']

        labels = {

            'nome': 'Nome Completo:',
            'sexo': 'Sexo:',
            'data_nascimento': 'Data de Nascimento:',
            'naturalidade': 'Naturalidade:',

            'nome_pai': 'Nome do Pai:',
            'nome_mae': 'Nome da Mãe:',

            'endereco': 'Endereço:',
            'cidade': 'Cidade:',
            'uf': 'UF:',

            'celular_pai': 'Celular do Pai:',
            'celular_mae': 'Celular da Mãe:',

            # Batismo
            'batizado': 'É Batizado?',
            'batizado_data': 'Data do Batismo:',
            'batizado_diocese': 'Diocese:',
            'batizado_paroquia': 'Paróquia:',
            'batizado_celebrante': 'Celebrante:',

            # 1ª Eucaristia
            'primeira_eucaristia': 'Fez a Primeira Eucaristia?',
            'primeira_eucaristia_data': 'Data da Primeira Eucaristia:',
            'primeira_eucaristia_diocese': 'Diocese:',
            'primeira_eucaristia_paroquia': 'Paróquia:',
            'primeira_eucaristia_celebrante': 'Celebrante:',

            'horario': 'Horário da Crisma:',

            'padrinho_nome': 'Nome do Padrinho/Madrinha:',
            'padrinho_celular': 'Celular do Padrinho/Madrinha:',
        }

        widgets = {

            # Dados principais
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'sexo': forms.Select(attrs={'class': 'form-select'}),
            'data_nascimento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'naturalidade': forms.TextInput(attrs={'class': 'form-control'}),

            # Filiação
            'nome_pai': forms.TextInput(attrs={'class': 'form-control'}),
            'nome_mae': forms.TextInput(attrs={'class': 'form-control'}),

            # Endereço
            'endereco': forms.TextInput(attrs={'class': 'form-control'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control'}),
            'uf': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 2}),

            # Contatos
            'celular_pai': forms.TextInput(attrs={'class': 'form-control'}),
            'celular_mae': forms.TextInput(attrs={'class': 'form-control'}),

            # Batizado
            'batizado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'batizado_data': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'batizado_diocese': forms.TextInput(attrs={'class': 'form-control'}),
            'batizado_paroquia': forms.TextInput(attrs={'class': 'form-control'}),
            'batizado_celebrante': forms.TextInput(attrs={'class': 'form-control'}),

            # Primeira Eucaristia
            'primeira_eucaristia': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'primeira_eucaristia_data': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'primeira_eucaristia_diocese': forms.TextInput(attrs={'class': 'form-control'}),
            'primeira_eucaristia_paroquia': forms.TextInput(attrs={'class': 'form-control'}),
            'primeira_eucaristia_celebrante': forms.TextInput(attrs={'class': 'form-control'}),

            'horario': forms.Select(attrs={'class': 'form-select'}),

            'padrinho_nome': forms.TextInput(attrs={'class': 'form-control'}),
            'padrinho_celular': forms.TextInput(attrs={'class': 'form-control'}),
            
               # Responsável
            'nome_responsavel': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf_responsavel': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '000.000.000-00'}),
            'endereco_responsavel': forms.TextInput(attrs={'class': 'form-control'}),
        }

        error_messages = {
            'nome': {'required': 'Informe o nome completo.'},
            'data_nascimento': {'required': 'Informe a data de nascimento.'},
            'endereco': {'required': 'Informe o endereço.'},
            'cidade': {'required': 'Informe a cidade.'},
            'uf': {'required': 'Informe o estado (UF).'},
        }

    def clean(self):
        cleaned_data = super().clean()

        # ======== Batismo ========
        if cleaned_data.get('batizado'):
            if not cleaned_data.get('batizado_data'):
                self.add_error('batizado_data', 'Informe a data do batismo.')
            if not cleaned_data.get('batizado_diocese'):
                self.add_error('batizado_diocese', 'Informe a diocese do batismo.')
            if not cleaned_data.get('batizado_paroquia'):
                self.add_error('batizado_paroquia', 'Informe a paróquia do batismo.')
            if not cleaned_data.get('batizado_celebrante'):
                self.add_error('batizado_celebrante', 'Informe o celebrante do batismo.')

        # ======== Primeira Eucaristia ========
        if cleaned_data.get('primeira_eucaristia'):
            if not cleaned_data.get('primeira_eucaristia_data'):
                self.add_error('primeira_eucaristia_data', 'Informe a data da primeira eucaristia.')
            if not cleaned_data.get('primeira_eucaristia_diocese'):
                self.add_error('primeira_eucaristia_diocese', 'Informe a diocese.')
            if not cleaned_data.get('primeira_eucaristia_paroquia'):
                self.add_error('primeira_eucaristia_paroquia', 'Informe a paróquia.')
            if not cleaned_data.get('primeira_eucaristia_celebrante'):
                self.add_error('primeira_eucaristia_celebrante', 'Informe o celebrante.')

        return cleaned_data
