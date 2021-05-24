from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class Chat(models.Model):
    DIALOG = 'D'
    CHAT = 'C'
    CHAT_TYPE_CHOICES = (
        (DIALOG, _('Dialog')),
        (CHAT, _('Chat'))
    )

    type = models.CharField(
        _('Тип'),
        max_length=1,
        choices=CHAT_TYPE_CHOICES,
        default=DIALOG
    )
    members = models.ManyToManyField(User, verbose_name=_("Member"))

    def get_absolute_url(self):
        return '/dialogs/%i/' % self.pk


class Message(models.Model):
    chat = models.ForeignKey(Chat, verbose_name=_("Chat"), on_delete=models.CASCADE,)
    author = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.CASCADE,)
    message = models.TextField(_("Message"))
    pub_date = models.DateTimeField(_('Message date'), default=timezone.now)
    is_readed = models.BooleanField(_('Readed'), default=False)

    class Meta:
        ordering = ['pub_date']

    def __str__(self):
        return self.message
