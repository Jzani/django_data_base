from django.db import models

# Create your models here.
class Topic(models.Model):
    topic_name=models.CharField(max_length=70,primary_key=True)

class Webpage(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=20)
    url=models.URLField()

class AcessRecord(models.Model):
    name=models.CharField( max_length=50)
    author=models.CharField(max_length=50)
    date=models.DateField()
