from django.db import models

from django.utils import timezone


class Schedule(models.Model):
    # author = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    title = models.CharField(max_length=200)
    # text = models.TextField()

    # def publish(self):
    #     self.published_date = timezone.now()
    #     self.save()

    # def __str__(self):
    #     return self.title

class Day(models.Model):
    dayofweek = models.TextField()
    one = models.TextField()
    two = models.TextField()
    three = models.TextField()
    four = models.TextField()
    five = models.TextField()
    six = models.TextField()
    seven = models.TextField()