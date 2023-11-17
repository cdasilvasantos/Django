from django.db import models

class TodoList(models.Model):
    this_item = models.TextField()
    time = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.this_item} - {self.time}"
