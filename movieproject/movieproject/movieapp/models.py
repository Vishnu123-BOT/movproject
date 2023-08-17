from django.db import models

class movie(models.Model):
    name=models.CharField(max_length=250)
    description=models.TextField()
    year=models.IntegerField()
    image=models.ImageField(upload_to='gallery')

    def __str__(self):
       return self.name