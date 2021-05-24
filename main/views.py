from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def template(request):
    return render(request, 'main/template.html')
