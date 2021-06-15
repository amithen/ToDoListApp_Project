from django.db import models


class ToDoListData(models.Model):
    title = models.CharField(max_length=56)

    def __str__(self):
        return self.title
