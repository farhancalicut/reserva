from django.db import models
from turf.models import Turf
from user.models import User
from booking.models import Booking
# Create your models here.
class Payment(models.Model):
    pay_id = models.AutoField(primary_key=True)
    amount = models.CharField(max_length=45)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    #booking_id = models.IntegerField()
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    status = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'payment'

