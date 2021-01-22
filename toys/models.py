from django.db import models


class Toy(models.Model):
    title = models.CharField(max_length=225)
    price = models.IntegerField()
    description = models.TextField()
    picture = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
