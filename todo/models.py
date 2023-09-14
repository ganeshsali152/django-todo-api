from django.db import models


class ToDo(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()

    class Meta:
        db_table = "todo"

    def __str__(self):
        return self.title
