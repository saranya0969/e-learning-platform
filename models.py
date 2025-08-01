from django.db import models

class Lesson(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    section = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
