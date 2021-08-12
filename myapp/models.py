from django.db import models


class Member(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    address = models.CharField(max_length=200)
    contact = models.CharField(max_length=50)

    def __str__(self):
        return self.name
