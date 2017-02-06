from django.db import models
from django.contrib.sites.models import Site
from django.contrib.auth.models import User


class Article(models.Model):
    headline = models.CharField(max_length=200)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    sites = models.ManyToManyField(Site)