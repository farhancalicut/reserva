from django.db import models
# Create your models here.
class Manager(models.Model):
    manager_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    address = models.CharField(max_length=100)
    qualification = models.CharField(max_length=45)
    password = models.CharField(max_length=8)
    status = models.CharField(max_length=45)


    class Meta:
        managed = False
        db_table = 'manager'

