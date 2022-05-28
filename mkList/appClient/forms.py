from dataclasses import Field
from tkinter import HIDDEN
from django import forms
from client.models import Cliente

class ClienteAdminForm(forms.ModelForm):
    class Meta:
        model= Cliente
        fields= '__all__'

    def __init__(self, *args, **kwargs):
        super(ClienteAdminForm, self).__init__(*args, **kwargs)
        #self.fields['usuario'].widget = forms.HiddenInput()

class ClienteForm(forms.ModelForm):
    class Meta:
        model= Cliente
        fields= '__all__'

    def __init__(self, *args, **kwargs):
        super(ClienteForm, self).__init__(*args, **kwargs)
        self.fields['usuario'].widget = forms.HiddenInput()

class ClienteNuevoForm(forms.ModelForm):
    
    class Meta:
        model= Cliente
        fields = ('nombre', 'rut', 'dv', 'direccion', 'comuna', 'ciudad', 'pais', 'fono',)

    def __init__(self, *args, **kwargs):
        super(ClienteNuevoForm, self).__init__(*args, **kwargs)
        #self.fields['usuario'].widget = forms.HiddenInput()
        #self.fields["usuario"].disabled = True
        #self.fields["usuario"].initial = 7