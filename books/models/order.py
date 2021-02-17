from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from six import python_2_unicode_compatible

__all__ = ('Order',)


@python_2_unicode_compatible
class Order(models.Model):
    """Order."""

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    lines = models.ManyToManyField('books.OrderLine', blank=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta(object):
        """Meta options."""

        ordering = ["-created"]

    def __str__(self):
        return _('Order')

    @property
    def created_indexing(self):
        return self.created.strftime(settings.ELASTICSEARCH_DATETIME_FORMAT)

    @property
    def updated_indexing(self):
        return self.updated.strftime(settings.ELASTICSEARCH_DATETIME_FORMAT)
