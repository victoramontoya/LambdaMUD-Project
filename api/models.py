from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User

# Create your models here.

# class Conversation(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     message = models.CharField(blank=True, null=True, max_length=225)
#     status = models.CharField(blank=True, null=True, max_length=225)
#     created_at = models.DateTimeField(auto_now=True)


# class Player(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
#     user = models.ForeignKey( User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=30)

#     def __str__(self):
#         return self.user.name