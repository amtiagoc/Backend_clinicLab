from django.db import models
from django_mysql.models import ListTextField

# Create your models here.
class Exams(models.Model):
    title = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    notes = ListTextField(
        base_field = models.CharField(max_length=500),
        size=100,  
    )
    created_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
    

    def __str__(self):
        return self.title