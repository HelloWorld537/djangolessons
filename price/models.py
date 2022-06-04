from django.db import models

# Create your models here.
class PriceCard(models.Model):
    pc_value = models.CharField(max_length=50, verbose_name="Price")
    pc_desc = models.CharField(max_length=50, verbose_name="Description")

    def __str__(self):
        return self.pc_desc
    
    class Meta:
        verbose_name = 'Price Card'
        verbose_name_plural = 'Prices Cards'

class PriceTable(models.Model):
    pc_title = models.CharField(max_length=50, verbose_name="Price Title")
    pc_old_price = models.CharField(max_length=50, verbose_name="Old Price")
    pc_new_price = models.CharField(max_length=50, verbose_name="New Price")


    def __str__(self):
        return self.pc_title
    
    class Meta:
        verbose_name = 'Services'
        verbose_name_plural = 'Services'