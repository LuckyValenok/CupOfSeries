from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import ContentsView, ContentView, terms, abuse, contacts

urlpatterns = [
    path('', ContentsView.as_view(), name='index'),
    path('terms', terms, name='terms'),
    path('abuse', abuse, name='abuse'),
    path('contacts', contacts, name='contacts'),
    path(r'view/<content_id>/', login_required(ContentView.as_view()), name='content'),
]
