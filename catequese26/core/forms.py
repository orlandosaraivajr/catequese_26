from django import forms
from django.forms import ModelForm
from .models import CatequeseInfantilModel, CrismaModel, Perseveranca_MEJ_Model, CatequeseAdultoModel


class CatequeseInfantilForm(ModelForm):
    class Meta:
        model = CatequeseInfantilModel
        fields = '__all__'
        exclude = ['ficha_impressa', 'ficha_impressa']

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

    def clean_nome(self):
        nome = self.cleaned_data.get('nome', '').strip()
        if len(nome.split()) < 2:
            raise forms.ValidationError("Erro: Digite o nome completo.")
        return nome

    def clean_nome_responsavel(self):
        nome = self.cleaned_data.get('nome_responsavel', '').strip()
        if len(nome.split()) < 2:
            raise forms.ValidationError("Erro: Digite o nome completo do responsável.")
        return nome

    def clean_nome_pai(self):
        nome = self.cleaned_data.get('nome_pai', '').strip()
        if len(nome.split()) < 2:
            raise forms.ValidationError("Erro: Digite o nome completo do pai.")
        return nome

    def clean_nome_mae(self):
        nome = self.cleaned_data.get('nome_mae', '').strip()
        if len(nome.split()) < 2:
            raise forms.ValidationError("Erro: Digite o nome completo da mãe.")
        return nome

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
        exclude = ['ficha_impressa', 'ficha_impressa']

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


class PerseverancaMejForm(ModelForm):
    class Meta:
        model = Perseveranca_MEJ_Model
        fields = '__all__'
        exclude = ['ficha_impressa', 'ficha_assinada']

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

            # Batizado
            'batizado': 'É Batizado?',
            'batizado_data': 'Data do Batismo:',
            'batizado_diocese': 'Diocese do Batismo:',
            'batizado_paroquia': 'Paróquia do Batismo:',
            'batizado_celebrante': 'Celebrante do Batismo:',

            # Primeira eucaristia
            'primeira_eucaristia': 'Já fez a Primeira Eucaristia?',
            'primeira_eucaristia_data': 'Data da Primeira Eucaristia:',
            'primeira_eucaristia_diocese': 'Diocese da Primeira Eucaristia:',
            'primeira_eucaristia_paroquia': 'Paróquia da Primeira Eucaristia:',
            'primeira_eucaristia_celebrante': 'Celebrante da Primeira Eucaristia:',
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

            # Batismo
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
            'nome': {'required': 'Informe o nome completo.'},
            'data_nascimento': {'required': 'Informe a data de nascimento.'},
            'endereco': {'required': 'Informe o endereço.'},
            'cidade': {'required': 'Informe a cidade.'},
            'uf': {'required': 'Informe a UF.'},
            'nome_pai': {'required': 'Informe o nome do pai.'},
            'nome_mae': {'required': 'Informe o nome da mãe.'},
            'celular_pai': {'required': 'Informe o celular do pai.'},
            'celular_mae': {'required': 'Informe o celular da mãe.'},
        }

    def clean_nome(self):
        nome = self.cleaned_data.get('nome', '').strip()
        if len(nome.split()) < 2:
            raise forms.ValidationError("Digite o nome completo.")
        return nome

    def clean_nome_responsavel(self):
        nome = self.cleaned_data.get('nome_responsavel', '').strip()
        if len(nome.split()) < 2:
            raise forms.ValidationError("Digite o nome completo do responsável.")
        return nome

    def clean_nome_pai(self):
        nome = self.cleaned_data.get('nome_pai', '').strip()
        if len(nome.split()) < 2:
            raise forms.ValidationError("Digite o nome completo do pai.")
        return nome

    def clean_nome_mae(self):
        nome = self.cleaned_data.get('nome_mae', '').strip()
        if len(nome.split()) < 2:
            raise forms.ValidationError("Digite o nome completo da mãe.")
        return nome

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


class CatequeseAdultoForm(forms.ModelForm):
    class Meta:
        model = CatequeseAdultoModel
        fields = '__all__'
        exclude = ['ficha_impressa', 'ficha_assinada']

        labels = {
            'nome': 'Nome Completo:',
            'cpf': 'CPF:',
            'sexo': 'Sexo:',
            'data_nascimento': 'Data de Nascimento:',
            'naturalidade': 'Naturalidade:',
            'celular': 'Celular:',

            'nome_pai': 'Nome do Pai:',
            'nome_mae': 'Nome da Mãe:',

            'endereco': 'Endereço:',
            'cidade': 'Cidade:',
            'uf': 'UF:',



            # Batizado
            'batizado': 'É Batizado?',
            'batizado_data': 'Data do Batismo:',
            'batizado_diocese': 'Diocese do Batismo:',
            'batizado_paroquia': 'Paróquia do Batismo:',
            'batizado_celebrante': 'Celebrante do Batismo:',

            # Primeira eucaristia
            'primeira_eucaristia': 'Já fez a Primeira Eucaristia?',
            'primeira_eucaristia_data': 'Data da Primeira Eucaristia:',
            'primeira_eucaristia_diocese': 'Diocese da Primeira Eucaristia:',
            'primeira_eucaristia_paroquia': 'Paróquia da Primeira Eucaristia:',
            'primeira_eucaristia_celebrante': 'Celebrante da Primeira Eucaristia:',

            # Casado
            'casado_igreja': "Casado na Igreja Católica Apostólica Romana ?",
            'casado_igreja_data': "Data casamento",
            'casado_igreja_diocese': "Diocese do casamento",
            'casado_igreja_paroquia': "Paróquia do casamento",
            'casado_igreja_celebrante': "Padre celebrante do casamento",
        }

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o nome completo'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '000.000.000-00'}),
            'sexo': forms.Select(attrs={'class': 'form-select'}),
            'data_nascimento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'naturalidade': forms.TextInput(attrs={'class': 'form-control'}),
            'celular': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(99)99999-9999'}),

            'nome_pai': forms.TextInput(attrs={'class': 'form-control'}),
            'nome_mae': forms.TextInput(attrs={'class': 'form-control'}),

            'endereco': forms.TextInput(attrs={'class': 'form-control'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control'}),
            'uf': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '2'}),
            'estado_civil': forms.TextInput(attrs={'class': 'form-control'}),

            'batizado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'batizado_data': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'batizado_diocese': forms.TextInput(attrs={'class': 'form-control'}),
            'batizado_paroquia': forms.TextInput(attrs={'class': 'form-control'}),
            'batizado_celebrante': forms.TextInput(attrs={'class': 'form-control'}),

            'primeira_eucaristia': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'primeira_eucaristia_data': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'primeira_eucaristia_diocese': forms.TextInput(attrs={'class': 'form-control'}),
            'primeira_eucaristia_paroquia': forms.TextInput(attrs={'class': 'form-control'}),
            'primeira_eucaristia_celebrante': forms.TextInput(attrs={'class': 'form-control'}),

            'casado_igreja': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'casado_igreja_data': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'casado_igreja_diocese': forms.TextInput(attrs={'class': 'form-control'}),
            'casado_igreja_paroquia': forms.TextInput(attrs={'class': 'form-control'}),
            'casado_igreja_celebrante': forms.TextInput(attrs={'class': 'form-control'}),

            'horario': forms.Select(attrs={'class': 'form-select'}),

            'padrinho_nome': forms.TextInput(attrs={'class': 'form-control'}),
            'padrinho_celular': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_nome(self):
        nome = self.cleaned_data.get('nome', '').strip()
        if len(nome.split()) < 2:
            raise forms.ValidationError("Digite o nome completo.")
        return nome

    def clean(self):
        cleaned = super().clean()

        # --- Validação do Batismo ---
        if cleaned.get('batizado'):
            campos = ['batizado_data', 'batizado_diocese', 'batizado_paroquia', 'batizado_celebrante']
            for campo in campos:
                if not cleaned.get(campo):
                    self.add_error(campo, "Campo obrigatório para quem é batizado.")

        # --- Validação da Primeira Eucaristia ---
        if cleaned.get('primeira_eucaristia'):
            campos = ['primeira_eucaristia_data', 'primeira_eucaristia_diocese',
                      'primeira_eucaristia_paroquia', 'primeira_eucaristia_celebrante']
            for campo in campos:
                if not cleaned.get(campo):
                    self.add_error(campo, "Campo obrigatório para quem já recebeu a Primeira Eucaristia.")

        # --- Validação de Casado na Igreja ---
        if cleaned.get('casado_igreja'):
            campos = ['casado_igreja_data', 'casado_igreja_diocese',
                      'casado_igreja_paroquia', 'casado_igreja_celebrante']
            for campo in campos:
                if not cleaned.get(campo):
                    self.add_error(campo, "Campo obrigatório para quem é casado na igreja.")

        return cleaned
