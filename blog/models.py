from django.db import models


class Category(models.Model):
    tittle = models.CharField(max_length=50)
