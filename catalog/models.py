from django.db import models

class Data(models.Model):
    qty = models.IntegerField()
    prod_desc = models.TextField()
    order_crtdate = models.DateTimeField()
    price_total = models.FloatField()
    rs = models.IntegerField()
    is_3d = models.TextField()
    def __str__(self):
        """String for representing the Model object."""
        return self.prod_desc
