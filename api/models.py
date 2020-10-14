from django.db import models

# Create your models here.


class CiscoData(models.Model):
    sapid=models.CharField(max_length=18)
    hostname=models.CharField(max_length=14)
    loopback=models.CharField(max_length=17)#here lenght 15 is suffient but I am consider now 17, ne
    macaddress=models.CharField(max_length=17)
    flag=models.BooleanField(default=True)

