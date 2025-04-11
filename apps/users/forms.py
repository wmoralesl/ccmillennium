from django import forms
from users.models import User 
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import ClearableFileInput

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'second_last_name', 'dpi','phone', 'birthdate', 'gender', 'photo', 'role', 'address']
        widgets = {
            'birthdate': forms.DateInput(attrs={
                'type': 'date',  
                'class': 'form-control',  
            },
             format='%Y-%m-%d'
             ),
             'photo': forms.FileInput(),
        }

class UserCreateForm(forms.ModelForm):
    # email = forms.EmailField(required=True)
    # date_of_birth = forms.DateField(
    #     widget=forms.DateInput(attrs={'type': 'date'}), 
    # )
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'second_last_name', 'phone', 'birthdate', 'email', 'gender', 'role')

        widgets = {
            'birthdate' : forms.DateInput(attrs={
                'type': 'date',  
                'class': 'form-control',  
            },
             format='%Y-%m-%d'
             ),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este correo electrónico ya está registrado.")
        return email
