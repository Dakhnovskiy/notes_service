from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=256)
    text = models.TextField()
    outer_user_id = models.IntegerField()

    def __str__(self):
        return self.title
