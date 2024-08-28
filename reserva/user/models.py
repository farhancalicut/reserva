from django.db import models

# Create your models here.

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    password = models.CharField(max_length=45)
    name = models.CharField(max_length=45)
    # age = models.CharField(max_length=10)
    contact_number = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'user'

