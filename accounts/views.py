from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, TemplateView
from .forms import SignUpForm, LoginForm


# Create your views here.

class SignUp(CreateView):
    form_class = SignUpForm
    template_name = 'accounts/signup.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            return redirect('gourmet:index')
        return render(request, 'accounts/signup.html', {'form': form})


# ログインビューのオーバライド方法は？？
class Login(LoginView):
    form_class = LoginForm
    template_name = 'accounts/login.html'


class Logout(LogoutView):
    template_name = 'accounts/logout.html'
