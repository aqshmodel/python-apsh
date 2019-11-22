from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from .forms import (LoginForm, RegisterForm)
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect


def index(request):
    context = {
        'user': request.user,
    }
    return render(request, 'index.html', context)


# def login(request):
#     context = {
#         'template_name': 'login.html',
#         'authentication_form': LoginForm
#     }
#     return auth_views.login(request, **context)
#
#
# def logout(request):
#     context = {
#         'template_name': 'index.html',
#     }
#     return auth_views.logout(request, **context)


@login_required
def profile(request):
    context = {
        'user': request.user,
    }
    return render(request, 'profile.html', context)


def regist(request):
    form = RegisterForm(request.POST or None)
    context = {
        'form': form,
    }
    return render(request, 'regist.html', context)


@require_POST
def regist_save(request):
    form = RegisterForm(request.POST)
    if form.is_valid():
        form.save(commit=True)
        return redirect('registration:index')

    context = {
        'form': form,
    }
    return render(request, 'regist.html', context)
