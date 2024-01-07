from django.db import models
from django.db.models import Model
from django.utils.translation import gettext as _
from parler.models import TranslatableModel, TranslatedFields


class Product(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=200),
        description=models.TextField(blank=True, null=True),
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products', blank=True, null=True)

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return self.name



