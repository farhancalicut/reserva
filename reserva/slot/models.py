from django.db import models
from turf.models import Turf

# Create your models here.


class Slot(models.Model):
    slot_id = models.AutoField(primary_key=True)
    slot = models.TimeField()
    e_time = models.TimeField()
    turf = models.ForeignKey(Turf,on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'slot'