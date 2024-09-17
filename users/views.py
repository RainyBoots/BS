from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from .forms import LoginForm, RegisterForm
from django.urls import reverse_lazy
from django.contrib.auth import logout


class LoginView(LoginView):
    template_name = 'login.html'
    form_class = LoginForm
    
    def get_success_url(self):
        return reverse_lazy('main')
    

class LogoutView(LogoutView):
    template_name = 'logout.html'   
    next_page = reverse_lazy('logout')

class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('main')