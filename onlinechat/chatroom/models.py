from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    phonenumber = models.CharField(max_length=20, unique=True, null=False)
    pass

    def __str__(self):
        return self.username
    
class Contacts(models.Model):
    id = models.AutoField(primary_key=True)
    user1 = models.CharField(max_length=20)
    user2 = models.CharField(max_length=20)
    status = models.CharField(max_length=20, default="pending")
    
    def serialize(self):
        return {
            "id": self.id,
            "user1": self.user1,
            "user2": self.user2,
            "status": self.status
        }
    
class Chat(models.Model):
    id = models.AutoField(primary_key=True)
    sender = models.CharField(max_length=20)
    reciever = models.CharField(max_length=20)
    message = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def serialize(self):
        return {
            "id": self.id,
            "sender": self.sender,
            "reciever": self.reciever,
            "message": self.message,
            "timestamp": self.timestamp
        }