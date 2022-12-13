from django.forms import ModelForm
from django import forms
from perpustakaan.models import Buku
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import TextInput,PasswordInput

class FormBuku(ModelForm) :
    class Meta:
        model = Buku
        fields = '__all__'

        widgets = {
            'judul' : forms.TextInput({'class' : 'form-control'}),
            'penulis' : forms.TextInput({'class' : 'form-control'}),
            'penerbit' : forms.TextInput({'class' : 'form-control'}),
            'jumlah' : forms.NumberInput({'class' : 'form-control'}),
            'keterangan' : forms.Select({'class' : 'form-control'}),
        }
        
