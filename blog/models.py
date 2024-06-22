from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50)

class Post(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField()
    text = models.TextField()
    category = models.ManyToOneRel(Category)

