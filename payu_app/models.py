from django.db import models


class UserDetails(models.Model):

    Email = models.EmailField(max_length=50, unique= True)
    Username = models.CharField(max_length=100, default='abc')
    Password = models.CharField(max_length=50)
    LastLoginDate = models.DateTimeField(auto_now=True)


class UserInput(models.Model):
    state_code = models.CharField(max_length=20)
    Type = [('c','C'),('s','S')]
    Type1 = [('g','G'),('p','P'),('u','U')]
    Refno = models.PositiveIntegerField(default=1)
    A_Type = models.CharField(choices=Type,max_length=1)
    D_Type = models.CharField(choices=Type1,max_length=1)
    result = models.TextField(max_length=50, default=0)
    created_date = models.DateField(auto_now=True)
