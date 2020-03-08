from django.db import models

# Create your models here.

class Question1(models.Model):
    word = models.CharField(max_length = 120)
    definitionWord = models.TextField()
    definitionOther1 = models.TextField()
    definitionOther2 = models.TextField()
    definitionOther3 = models.TextField()
    definitionOther4 = models.TextField()