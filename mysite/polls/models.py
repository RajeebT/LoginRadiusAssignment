from django.db import models

# Create your models here.

from django.db import models


class Candidates(models.Model):
    Name = models.CharField(max_length=30)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.Name

    def Number_Of_Votes(self):
         return self.votes
