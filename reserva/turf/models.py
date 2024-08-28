from django.db import models
from manager.models import Manager

# Create your models here.
class Turf(models.Model):
    turf_id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=8)
    turf_name = models.CharField(max_length=45)
    place = models.CharField(max_length=45)
    categoty = models.CharField(max_length=45)
    status = models.CharField(max_length=45)
    price = models.CharField(max_length=45)
    image = models.CharField(max_length=450)
    longitude = models.CharField(max_length=45)
    latitude = models.CharField(max_length=45)
    # manager_id = models.IntegerField()
    manager=models.ForeignKey(Manager,on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'turf'
