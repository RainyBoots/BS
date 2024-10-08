from django import forms
from .models import Visit
import re


class VisitModelForm (forms.ModelForm):
    class Meta:
        model = Visit
        fields = ['client_name', 'phone', 'master', 'service']
        widgets = {
            'client_name': forms.TextInput(attrs={'placeholder': 'Имя', 'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'type': 'tel', 'placeholder': 'Номер телефона', 'class': 'form-control'}),
            'master': forms.Select(attrs={'class': 'form-control'}),
            'services': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }
        


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if self.errors.get(field_name):
                widget_classes = field.widget.attrs.get('class', '')
                field.widget.attrs['class'] = f'{widget_classes} is-invalid'
                
    
    def clean_phone(self):
        phone = self.cleaned_data.get('phone', '').strip()

        phone_pattern = r'^(\+7|8)\d{10}$'
        if not re.match(phone_pattern, phone):
            raise forms.ValidationError('Номер телефона должен начинаться с +7 или с 8 и содержать 10 цифр после кода страны.')

        return phone
    
    def clean(self):
        cleaned_data = super().clean()
        master = cleaned_data.get("master")
        service = cleaned_data.get("service")

        if master and service:
            if not master.services.filter(id=service.id).exists():
                raise forms.ValidationError(f'Мастер {master} не предоставляет услугу {service}.')

        return cleaned_data
    
