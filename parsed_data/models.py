from django.db import models
from django.urls import reverse

# Create your models here.
class Link(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField(unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('link-detail', args=[str(self.id)])


class Member(models.Model):
    nickname_text = models.CharField(max_length=30)

    def __str__(self):
        return self.nickname_text

    # Metadata
    class Meta:
        ordering = ['nickname_text']

    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('member-detail', args=[str(self.id)])

class Cmt(models.Model):
    nickname = models.ForeignKey(Member, on_delete=models.CASCADE)
    comment = models.TextField()
    date = models.CharField(max_length=20)
    link = models.URLField()

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('cmt-detail', args=[str(self.id)])