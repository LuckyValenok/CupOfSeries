from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import ContentsView

urlpatterns = [
    path('', ContentsView.as_view(), name='index'),
    # path(r'/<content_id>/', login_required(MessagesView.as_view()), name='content'),
]
