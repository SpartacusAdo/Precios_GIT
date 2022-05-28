from django import forms
from django.forms.widgets import TextInput


from .models import Categoria, Color, Bulbo

#--------------------------------------------------------------------------------------------
class CategoriaForm(forms.ModelForm):
    class Meta:
        model= Categoria
        fields= '__all__'

        widgets = {
            'categoria' : TextInput(attrs={"class":"form-control mb-3", 
                                        "placeholder":"Ingresar",
                                        "autocomplete":"off"}),

            'slug' : TextInput(attrs={"class":"form-control mb-3", 
                                        "placeholder":"Ingresar slug",
                                        "autocomplete":"off"}),

            'orden' : forms.NumberInput(attrs={"class":"form-control mb-3",}),
           
        }

#--------------------------------------------------------------------------------------------
class ColorForm(forms.ModelForm):
    class Meta:
        model= Color
        fields= '__all__'

        widgets = {
            'color' : TextInput(attrs={"class":"form-control mb-3", 
                                        "placeholder":"Ingresar",
                                        "autocomplete":"off"}),
           
        }

#----------------------------------------------------------------------------------------------
class BulboForm(forms.ModelForm):
    class Meta:
        model= Bulbo
        fields= '__all__'

        widgets = {

            'image': forms.ClearableFileInput(attrs={'class': 'form-control form-control-sm mb-3',
                                                        }),
            'thumbnail': forms.ClearableFileInput(attrs={'class': 'form-control form-control-sm mb-3',
                                                        }),
            
        }

    def __init__(self, *args, **kwargs):
        super(BulboForm, self).__init__(*args, **kwargs)
        #self.fields['usuario'].widget = forms.HiddenInput()
        #self.fields["codigo"].disabled = True