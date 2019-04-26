from django.db import models


class Member(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    url = models.URLField(max_length=200, null=True, blank=True)
    follower = models.IntegerField()
