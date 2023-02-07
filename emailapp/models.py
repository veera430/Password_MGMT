from django.db import models

class Article(models.Model):
    title = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.title
