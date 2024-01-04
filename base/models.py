from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=30)
    desc=models.TextField(max_length=150,blank=True)
    complete=models.BooleanField(default=False)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering=['complete']