from django.db import models

# Create your models here.


class Data(models.Model):

    search = models.TextField(max_length=10000)

    def __str__(self):
        return self.search


