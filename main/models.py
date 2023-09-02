from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Friend(models.Model):
    RELATION_CHOICES = (
        ('Friend', 'Friend'),
        ('Family', 'Family'),
        ('Relative', 'Relative'),
        ('Colleague', 'Colleague'),
        ('Other', 'Other'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    relation_type = models.CharField(max_length=20, choices=RELATION_CHOICES, default='Friend')
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    photo = models.ImageField(upload_to='photos/', blank=True)
    priority = models.IntegerField(default=1)
    talked = models.BooleanField(default=False)
    last_contact = models.DateField(blank=True, null=True)
    notes = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
