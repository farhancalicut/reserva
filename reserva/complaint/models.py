from django.db import models
from user.models import User
# Create your models here.
class Complaint(models.Model):
    comp_id = models.AutoField(primary_key=True)
    complaint = models.CharField(max_length=45)
    date_time = models.DateTimeField()
    replay = models.CharField(max_length=45,null=True)
    status = models.CharField(max_length=100)
    #user_id = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'complaint'