from django.db import models

# Create your models here.
class Task_Model(models.Model):

    task=models.CharField(max_length=100)
    period=models.IntegerField()
    status=models.BooleanField(default=False)

    def __str__(self):
        return self.task