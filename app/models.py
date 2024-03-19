
from django.db import models

class Student(models.Model):
    CHOICES = [
        ('skasc', 'SKASC'),
        ('hindustan', 'Hindustan')
    ]
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    clg_name = models.CharField(max_length=50, choices=CHOICES)
    
    class Meta:
        db_table = "students"
        
    def __str__(self):
        return self.name
