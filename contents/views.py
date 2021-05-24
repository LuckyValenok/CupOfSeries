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

        if content is not None:
            content.views += 1
            content.save()

        return render(request, 'contents/content.html', {'content': content})


def terms(request):
    return render(request, 'contents/terms.html')


def abuse(request):
    return render(request, 'contents/abuse.html')


def contacts(request):
    return render(request, 'contents/contacts.html')
