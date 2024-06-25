from django.db import models


class Category(models.Model):
    tittle = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.tittle


class Post(models.Model):
    title = models.CharField(max_length=150)
    categories = models.ManyToManyRel(Category)
    post_text = models.TextField()
    image = models.ImageField(null=True, blank=True)
    published_date = models.DateField()


class Project(models.Model):
    project_statement = {
        1: "in planning",
        2: "in developing",
        3: "finished",
        4: "abandoned"
    }
    name = models.CharField(max_length=150)
    logo = models.ImageField(null=True, default=True)
    description = models.TextField()
    condition = None  # write right choices expression
    images = None  # Can I store several image like project example?
    start_date = models.DateField()
    finish_date = models.DateField()
