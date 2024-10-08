from django.db import models
import datetime

# Create your models here.
class addNote(models.Model):
    username = models.CharField(max_length=14)
    email = models.EmailField()
    title = models.CharField(max_length=30)
    desc = models.CharField(max_length=500)
    # date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.username
    