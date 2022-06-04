from django.db import models

class StatusCrm(models.Model):
    Status_name = models.CharField(max_length=200, verbose_name='Title Status')

    def __str__(self):
        return self.Status_name
    class Meta:
        verbose_name = 'tatus'
        verbose_name_plural = 'tatuts'

# Create your models here.
class Order(models.Model):
    order_dt = models.DateTimeField(auto_now=True)
    order_name = models.CharField(max_length=100, verbose_name='Name')
    order_phone = models.CharField(max_length=100)
    order_status = models.ForeignKey(StatusCrm, on_delete=models.PROTECT, null=True, blank = True, verbose_name='StatusP')

    def __str__(self):
        return self.order_name
    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

class ComentCrm(models.Model):
    coment_binding = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Zayvkka')
    coment_text = models.TextField(verbose_name='text coment')
    coment_date = models.DateTimeField(auto_now = True, verbose_name='text coment')

    def __str__(self):
        return self.coment_text
    class Meta:
        verbose_name = 'Coment88'
        verbose_name_plural = 'comments'


