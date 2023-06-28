from django.db import models

# Create your models here.

class Member(models.Model):
    id = models.CharField(primary_key=True, max_length=15)
    password = models.CharField(max_length=15)
    name = models.CharField(max_length=10)
    gender = models.CharField(max_length=5)
    email = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'member'