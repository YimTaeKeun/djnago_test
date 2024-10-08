from django.db import models

# Create your models here.

class Human(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

