from django.forms import ModelForm, Textarea
from django import forms
from .models import dictclass

class DictForm(forms.ModelForm):
    class Meta:
        model = dictclass
        fields = ['id', 'Ordem', 'palavra', 'palavratrad', 'frase', 'frasetrad', 'frase2',
                  'frasetrad2', 'frase3', 'frasetrad3', 'frase4', 'frasetrad4', 'frase5', 'frasetrad5',
                  'qualtabela2', 'title',
                  'figura1', 'som1', 'suaresposta1', 'suaresposta2', 'suaresposta3', 'ondetabela',
                  'Acertou', 'Corretas', 'Porcentagem', 'Jafoi']
        #'tipo_audio'
        #TIPOAUDIO = [('ingles', 'ingles'), ('alemao', 'alemao')]

        widgets = {'id': forms.TextInput(attrs={'size': 5}),
                   'Ordem': forms.TextInput(attrs={'size': 70}),
                   'palavra': forms.TextInput(attrs={'size': 70}),
                   'palavratrad': forms.TextInput(attrs={'size': 70}),
                   'frase': forms.TextInput(attrs={'size': 70}),
                   'frasetrad': forms.TextInput(attrs={'size': 70}),
                   'frase2': forms.TextInput(attrs={'size': 70}),
                   'frasetrad2': forms.TextInput(attrs={'size': 70}),
                   'frase3': forms.TextInput(attrs={'size': 70}),
                   'frasetrad3': forms.TextInput(attrs={'size': 70}),
                   'frase4': forms.TextInput(attrs={'size': 70}),
                   'frasetrad4': forms.TextInput(attrs={'size': 70}),
                   'frase5': forms.TextInput(attrs={'size': 70}),
                   'frasetrad5': forms.TextInput(attrs={'size': 70}),
                   'figura1': forms.TextInput(attrs={'size': 70}),
                   'som1': forms.TextInput(attrs={'size': 70}),
                   'suaresposta1': forms.TextInput(attrs={'size': 70}),
                   'suaresposta2': forms.TextInput(attrs={'size': 70}),
                   'suaresposta3': forms.TextInput(attrs={'size': 70}),
                   'qualtabela2': forms.TextInput(attrs={'size': 70}),
                   'ondetabela': forms.TextInput(attrs={'size': 70}),
                   'title': forms.TextInput(attrs={'size': 70}),
                   'Acertou': forms.TextInput(attrs={'size': 3}),
                   'Corretas': forms.TextInput(attrs={'size': 3}),
                   'Porcentagem': forms.TextInput(attrs={'size': 3}),
                   'Jafoi': forms.TextInput(attrs={'size': 3}),

                   }

class MudarTabelaForm(forms.ModelForm):
    class Meta:
        model = dictclass
        fields = ['qualtabela2']
        widgets = {
                   'qualtabela2': forms.TextInput(attrs={'size': 70}),
                   }

class DictForm2(forms.ModelForm):
    class Meta:
        model = dictclass
        fields = ['palavra', 'palavratrad', 'frase', 'frasetrad', 'frase2',
                  'frasetrad2', 'frase3', 'frasetrad3', 'frase4', 'frasetrad4', 'frase5', 'frasetrad5']

        widgets = {'palavra': forms.TextInput(attrs={'size': 70}),
                   'palavratrad': forms.TextInput(attrs={'size': 70}),
                   'frase': forms.TextInput(attrs={'size': 70}),
                   'frasetrad': forms.TextInput(attrs={'size': 70}),
                   'frase2': forms.TextInput(attrs={'size': 70}),
                   'frasetrad2': forms.TextInput(attrs={'size': 70}),
                   'frase3': forms.TextInput(attrs={'size': 70}),
                   'frasetrad3': forms.TextInput(attrs={'size': 70}),
                   'frase4': forms.TextInput(attrs={'size': 70}),
                   'frasetrad4': forms.TextInput(attrs={'size': 70}),
                   'frase5': forms.TextInput(attrs={'size': 70}),
                   'frasetrad5': forms.TextInput(attrs={'size': 70}),
                   }

class DictForm_Novo(forms.ModelForm):
    class Meta:
        model = dictclass
        fields = ['palavra', 'palavratrad', 'frase', 'frasetrad', 'frase2',
                  'frasetrad2', 'frase3', 'frasetrad3', 'frase4', 'frasetrad4', 'frase5', 'frasetrad5']


        widgets = {'palavra': forms.TextInput(attrs={'size': 70}),
                   'palavratrad': forms.TextInput(attrs={'size': 70}),
                   'frase': forms.TextInput(attrs={'size': 70}),
                   'frasetrad': forms.TextInput(attrs={'size': 70}),
                   'frase2': forms.TextInput(attrs={'size': 70}),
                   'frasetrad2': forms.TextInput(attrs={'size': 70}),
                   'frase3': forms.TextInput(attrs={'size': 70}),
                   'frasetrad3': forms.TextInput(attrs={'size': 70}),
                   'frase4': forms.TextInput(attrs={'size': 70}),
                   'frasetrad4': forms.TextInput(attrs={'size': 70}),
                   'frase5': forms.TextInput(attrs={'size': 70}),
                   'frasetrad5': forms.TextInput(attrs={'size': 70}),
                   }

class DictForm_Busca(forms.ModelForm):
    class Meta:
        model = dictclass
        fields = ['title']
        widgets = {'title': forms.TextInput(attrs={'size': 70}),}

class DictForm_suaresposta(forms.ModelForm):
    class Meta:
        model = dictclass
        fields = ['suaresposta1']
        widgets = {'suaresposta1': forms.TextInput(attrs={'size': 70}),}

class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = dictclass
        fields = ('title', 'image')


"""
class TipoAudio(forms.ModelForm): 
    TIPOAUDIO = [('ingles', 'ingles'), ('alemao', 'alemao')]
    campo_doisaudios = forms.CharField(widget=forms.RadioSelect(choices=TIPOAUDIO))

    class Meta:
        model = ForensicTraffic
        fields = ['campo_doisaudios']
"""