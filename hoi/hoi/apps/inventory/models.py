from django.db import models
from django.dispatch import receiver
from model_utils.models import TimeFramedModel

class Item(models.Model):
    item_code = models.CharField("codigo de producto", max_length=64, null=False, blank=False,
                                 unique=True, help_text='Codigo unico para identificar este producto')
    name = models.CharField("nombre del producto", max_length=128, null=False, blank=False, help_text='Nombre de este producto')
    cost = models.PositiveIntegerField('costo del producto', null=False, blank=False)
    is_out = models.BooleanField("sin inventario?", null=False, blank=False, default=False)
    def __unicode__(self):
        return self.name

    @property
    def inventario(self):
        s = ItemChange.objects.filter(item=self).aggregate(inventario=models.Sum('delta'))
        return s['inventario']

    @property
    def costo_total(self):
        s = self.itemchange_set.all()
        return self.cost*sum(x.delta for x in s if x.delta > 0)

    # @property
    # def is_out(self):
    #     return self.inventario() == 0

class ItemChange(models.Model):
    date = models.DateTimeField("fecha de cambio", null=False, blank=False, help_text='Fecha en que se realiza el cambio')
    item = models.ForeignKey(Item, null=False, blank=False)
    delta = models.IntegerField("cambio realizado", null=False, blank=False, help_text='Cambio a realizar. Un cambio positivo denota compra o adquisicion de productos. Cambio negativo indica uso o perdida de producto.')

    def __unicode__(self):
        return "Cambio en %s el %s" % (self.item, self.date)


@receiver(models.signals.post_save, sender=ItemChange)
def update_status(sender, instance, **kw):
    instance.item.is_out = instance.item.inventario == 0
    instance.item.save()

# Create your models here.
