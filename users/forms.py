from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя пользователя'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}))


class RegisterForm(UserCreationForm):
    username_or_email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя пользователя или Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}), help_text='')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Подтверждение пароля'}))

    class Meta:
        model = get_user_model()
        fields = ('username_or_email', 'password1', 'password2')

    def clean_username_or_email(self):
        data = self.cleaned_data['username_or_email']
        if "@" in data:
            try:
                validate_email(data)
            except ValidationError:
                raise ValidationError("Введён некорректный адрес электронной почты.")
        else:
            if len(data) < 5:
                raise ValidationError("Имя пользователя должно содержать не менее 5 символов.")
        
        return data
    
    def save(self, commit=True):
        user = super().save(commit=False)
        if '@' in self.cleaned_data['username_or_email']:
            user.email = self.cleaned_data['username_or_email']  
            user.username = self.cleaned_data['username_or_email']  
        else:
            user.username = self.cleaned_data['username_or_email']
        
        if commit:
            user.save()
        return user