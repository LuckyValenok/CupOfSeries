from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import ContentsView, ContentView

urlpatterns = [
    path('', ContentsView.as_view(), name='index'),
    path(r'/view/<content_id>/', login_required(ContentView.as_view()), name='content'),
]
