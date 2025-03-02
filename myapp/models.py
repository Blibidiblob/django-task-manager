# Create your models here.

from django.db import models

IMPORTANCE_CHOICES = [
    ('high', '🦄 Very Important'),
    ('medium', '🍦 Normal Importance'),
    ('low', '🦡 Not So Important'),
]

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)  # Optional description
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(blank=True, null=True)  # New due date field!
    tag = models.CharField(max_length=50, blank=True, null=True)  # New tag field!
    importance = models.CharField(max_length=10, choices=IMPORTANCE_CHOICES, default='medium')
    annoying = models.BooleanField(default=False)  # 💩 Annoying task checkbox!
    def __str__(self):
        return self.title



