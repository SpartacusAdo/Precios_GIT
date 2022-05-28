from django.forms import ModelForm  # Importar modelforms
from django.contrib.auth.forms import UserCreationForm     # Esto es para login and register
from django.contrib.auth.models import User                # Esto es para login and register




class CreateUserForm(UserCreationForm):    # Usamos lo importado
    class Meta:                            # El resto es lo mismo
        model=User
        fields =['username', 'email', 'password1', 'password2']