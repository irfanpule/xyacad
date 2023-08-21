import sweetify
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    sweetify.toast(
        request, 'Welcome to home page', icon='info', persistent="Bye toast!")
    return render(request, 'dashboard/home.html')


def form_general(request):
    return render(request, 'dashboard/two-column-form.html')
