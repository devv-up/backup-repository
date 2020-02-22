from django.db import models

# Create your models here.


class member(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=12, db_index=True)
    password = models.CharField(max_length=128)
    email = models.CharField(db_index=True, max_length=128)
    verification = models.BooleanField()
    verification_key = models.CharField(max_length=128)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    is_superuser = models.BooleanField()
    last_login = models.DateTimeField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    date_joined = models.DateTimeField()
    profile_photo = models.CharField(max_length=4096)