from django.db import models
from manager.models import Manager
from turf.models import Turf
# Create your models here.
class AssignManager(models.Model):
    assign_id = models.AutoField(primary_key=True)
    # manager_id = models.IntegerField()
    manager=models.ForeignKey(Manager, on_delete=models.CASCADE)
    #turf_id = models.IntegerField()
    turf=models.ForeignKey(Turf, on_delete=models.CASCADE)
    date = models.DateTimeField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'assign_manager'
