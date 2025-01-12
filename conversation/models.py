from django.db import models
from item.models import Item
from django.contrib.auth.models import User

class Conversation(models.Model):
    item = models.ForeignKey(Item,related_name='conversations',on_delete=models.CASCADE)
    members = models.ManyToManyField(User,related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_At = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-modified_at',)

# class ConversationMessage(models.Model):