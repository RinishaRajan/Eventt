from django.db import models




# Create your models here.
class person(models.Model):
    Name = models.CharField(max_length=50,default="")
    Address = models.CharField(max_length=50,default="")
    Mobile = models.IntegerField(default="")
    Education = models.CharField(max_length=80,default="")
    Email = models.CharField(max_length=25,default="")


gender_choice =  (('f','female'),('m','male'))
event_choice =  (('m','marriage'),('b','birthday'),('p','pubberty'))


class Datas(models.Model):
    Name = models.CharField(max_length=50,default="")
    Address = models.CharField(max_length=50,default="")
    Mobile = models.CharField(max_length=50,default="")
    Gender = models.CharField(choices=gender_choice,max_length=128,default="")
    Event = models.CharField(choices=event_choice,max_length=128,default="")
    Email = models.CharField(max_length=20,default="")
    Event = models.CharField(max_length=20,default="")
    
    




    
    
