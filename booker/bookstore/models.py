from __future__ import unicode_literals

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category)
    description = models.TextField()
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.name
