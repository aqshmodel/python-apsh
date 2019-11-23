from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .forms import (RegisterForm, JobSeekerForm, DesiredConditionForm)


def index(request):
    context = {
        'user': request.user,
    }
    return render(request, 'index.html', context)

#
#
# def logout(request):
#     context = {
#         'template_name': 'index.html',
#     }
#     return auth_views.logout(request, **context)


def profile(request):
    context = {
        'user': request.user,
    }
    return render(request, 'profile.html', context)


@login_required
def role(request):
    context = {
        'user': request.user,
    }
    return render(request, 'role.html', context)


def desired_condition(request):
    form = DesiredConditionForm(request.POST or None)
    context = {
        'form': form,
        'user': request.user,
    }
    return render(request, 'desired_condition.html', context)


@require_POST
def desired_condition_save(request):
    form = DesiredConditionForm(request.POST)
    if form.is_valid():
        form.save(commit=True)
        return redirect('role.html')

    context = {
        'form': form,
    }
    return render(request, 'desired_condition.html', context)


def jobseeker(request):
    form = JobSeekerForm(request.POST or None)
    context = {
        'form': form,
        'user': request.user,
    }
    return render(request, 'jobseeker.html', context)


@require_POST
def jobseeker_save(request):
    form = JobSeekerForm(request.POST)
    if form.is_valid():
        form.save(commit=True)
        return redirect('role.html')

    context = {
        'form': form,
    }
    return render(request, 'jobseeker.html', context)


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
        return redirect('role.html')

    context = {
        'form': form,
    }
    return render(request, 'regist.html', context)
