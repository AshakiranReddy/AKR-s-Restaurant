from django.db import models

class AdminLoginModel(models.Model):
    username=models.CharField(max_length=30,unique=True)
    password=models.CharField(max_length=30)
    otp=models.IntegerField()


class StateModel(models.Model):
    stateno = models.AutoField(primary_key=True)
    statename = models.CharField(unique=True,max_length=30)

    def __str__(self):
        return self.statename

class CityModel(models.Model):
    cityno = models.AutoField(primary_key=True)
    cityname= models.CharField(max_length=30,unique=True)
    state= models.ForeignKey(StateModel,on_delete=models.CASCADE)

    def __str__(self):
        return self.cityname

class AreaModel(models.Model):
    area_no = models.AutoField(primary_key=True)
    area_name = models.CharField(max_length=50)
    city = models.ForeignKey(CityModel,on_delete=models.CASCADE)
