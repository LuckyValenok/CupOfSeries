from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import DialogsView, CreateDialogView, MessagesView

urlpatterns = [
    path(r'dialogs/', login_required(DialogsView.as_view()), name='dialogs'),
    path(r'dialogs/create/<user_id>/', login_required(CreateDialogView.as_view()), name='create_dialog'),
    path(r'dialogs/<chat_id>/', login_required(MessagesView.as_view()), name='chats'),
]
