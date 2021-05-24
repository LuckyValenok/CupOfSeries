from django.shortcuts import render
from django.views import View

from .models import Content


class ContentsView(View):
    def get(self, request):
        return render(request, 'contents/index.html', {'contents': Content.objects.all()})


class ContentView(View):
    def get(self, request, content_id):
        try:
            content = Content.objects.get(id=content_id)
        except Content.DoesNotExist:
            content = None

        return render(request, 'contents/template.html', {'content': content})


def terms(request):
    return render(request, 'contents/terms.html')


def abuse(request):
    return render(request, 'contents/abuse.html')


def contacts(request):
    return render(request, 'contents/contacts.html')
