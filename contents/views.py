from django.shortcuts import render
from django.views import View

from .models import Content


class ContentsView(View):
    def get(self, request):
        return render(request, 'main/index.html', {'contents': Content.objects.all()})
