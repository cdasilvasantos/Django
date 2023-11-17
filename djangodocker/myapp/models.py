from django.db import models



class todoList(models.Model):
    this_item = models.CharField(max_length=50)
    time = models.CharField(max_length=50)


