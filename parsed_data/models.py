from django.db import models

# Create your models here.
class LinkData(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField(unique=True)

    def __str__(self):
        return self.title

class CmtData(models.Model):
    nickname = models.CharField(max_length=30)
    comment = models.CharField(max_length=300)

    def __str__(self):
        return self.nickname