from django.db import models

class Blog_post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    linked_post = models.ForeignKey(Blog_post, on_delete=models.CASCADE)
    content = models.TextField()
    created_date = models.DateTimeField()
