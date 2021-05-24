from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class Content(models.Model):
    name = models.TextField(_('Content name'), default='')
    series = models.TextField(_('Content series'), default=1)
    season = models.TextField(_('Content season'), default=1)
    pub_date = models.DateTimeField(_('Content date'), default=timezone.now)
    views = models.IntegerField(_('Content views'), default=0)
    path = models.URLField(_('Content path'), default=0)
    cover = models.URLField(_('Content background'), default=0)

    def get_absolute_url(self):
        return '/view/%i/' % self.pk
