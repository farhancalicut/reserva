from django.db import models
from turf.models import Turf
# Create your models here.
class PriceDetails(models.Model):
    price_id = models.AutoField(primary_key=True)
    #turf_id = models.IntegerField()
    turf = models.ForeignKey(Turf, on_delete=models.CASCADE)
    price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'price_details'

