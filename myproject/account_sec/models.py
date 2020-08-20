from django.db import models
from django import forms

# Create your models here.

class User(models.Model):

    branch_choices = (
        ('cse','CSE'),
        ('mechanical','MECHANICAL'),
        ('civil','CIVIL'),
    )
    passout_year_choices = (
        ('2020','2020'),
        ('2021','2021'),
        ('2022','2022'),
        ('2023','2023'),
    )

    regdno = models.IntegerField(null=False,blank=False,unique=True)
    fullname = models.CharField(null=False,blank=False,max_length=30)
    email = models.EmailField(null=False,blank=False)
    password = models.CharField(max_length=20,null=False,blank=False)
    confirm_password = models.CharField(max_length=20,null=False,blank=False)
    contactno = models.IntegerField(null=True,blank=True)
    branch = models.CharField(max_length=20,choices=branch_choices)
    passout_year = models.CharField(max_length=20,choices=passout_year_choices)
    

    def __str__(self):
        return self.regdno