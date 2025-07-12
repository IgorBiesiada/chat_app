from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class FriendRequest(models.Model):
    
    STATUS_CHOICES = (
        (1, 'Pending'),
        (2, 'Accepted'),
        (3, 'Rejected'),
    )
    
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipient')
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    sent_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('sender', 'recipient')