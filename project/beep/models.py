from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length= 50)
    username = models.CharField(max_length= 20, unique= True)
    email = models.EmailField(unique= True)

class Event(models.Model):
    name = models.CharField(max_length= 50)
    begin = models.DateTimeField()
    location = models.TextField()
    desc = models.TextField(max_length= 300)
    creator = models.ForeignKey(User, to_field= 'username', on_delete= models.CASCADE)

class Attendee(models.Model):
    event = models.ForeignKey(Event, on_delete= models.CASCADE)
    name = models.ForeignKey(User, to_field= 'username', on_delete= models.CASCADE, related_name= 'attendents_name')
    email = models.ForeignKey(User, to_field= 'email', on_delete= models.CASCADE, related_name= 'attendents_email')