from django.shortcuts import render


def home(request):
    return render(request, 'ui/home.html')


def form_general(request):
    return render(request, 'ui/container-form.html')
