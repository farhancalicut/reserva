from django.db import models
from turf.models import Turf
from user.models import User
# Create your models here.
class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    date = models.DateField()    
    start_time = models.TimeField()
    end_time = models.TimeField()
    status = models.CharField(max_length=45)
    #turf_id = models.IntegerField(blank=True, null=True)
    turf = models.ForeignKey(Turf, on_delete=models.CASCADE)
    cancel_status = models.CharField(max_length=45)
    # user_id = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    class Meta:
        managed = False
        db_table = 'booking'

