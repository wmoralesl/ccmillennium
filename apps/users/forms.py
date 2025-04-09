from django import forms
from users.models import User 
from django.contrib.auth.forms import UserCreationForm

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'second_last_name', 'dpi','phone', 'birthdate', 'gender', 'photo', 'role', 'address']
        widgets = {
            'birthdate': forms.DateInput(attrs={
                'type': 'date',  
                'class': 'form-control',  
            }),
        }

class CustomUserCreationForm(UserCreationForm):
    # email = forms.EmailField(required=True)
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}), 
    )
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'second_last_name', 'phone', 'birthdate', 'email', 'gender', 'password1', 'password2', 'role')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este correo electrónico ya está registrado.")
        return email
