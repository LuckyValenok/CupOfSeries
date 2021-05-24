from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class Content(models.Model):
    name = models.TextField(_('Content name'), default='')
    series = models.IntegerField(_('Content series'), default=1)
    season = models.IntegerField(_('Content season'), default=1)
    pub_date = models.DateTimeField(_('Content date'), default=timezone.now)
    views = models.IntegerField(_('Content views'), default=0)
    path = models.URLField(_('Content path'))
    cover = models.URLField(_('Content background'))
    duration = models.IntegerField(_('Content duration'), default=1)

    def get_absolute_url(self):
        return '/view/%i/' % self.pk
