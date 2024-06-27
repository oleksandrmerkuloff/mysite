from django.db import models


class Category(models.Model):
    tittle = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.tittle


class Post(models.Model):
    title = models.CharField(max_length=150)
    categories = models.ManyToManyField(Category)
    post_text = models.TextField()
    image = models.ImageField(null=True, blank=True)
    published_date = models.DateField(auto_now_add=True)


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
    condition = models.IntegerField(choices=project_statement)
    start_date = models.DateField(auto_now_add=True)


class ProjectImages(models.Model):
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="images"
    )
    image = models.ImageField()
