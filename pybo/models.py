from django.db import models

class Question(models.Model):
    question = models.CharField(max_length=200)
    subject = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.question

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    subject = models.TextField()
    create_date = models.DateTimeField()

