from django.db import models

# Create your models here.
class ToDo(models.Model):
    def __str__(self):
        return self.Title
    
    Title = models.CharField(max_length=100,blank=False)
    Completed = models.BooleanField(default=False) 
    

    