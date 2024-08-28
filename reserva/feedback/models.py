from django.db import models
from user.models import User
# Create your models here.
class Feedback(models.Model):
    idfeedback_id = models.IntegerField(primary_key=True)
    feedback = models.CharField(max_length=45)
    # user_id = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        managed = False
        db_table = 'feedback'
