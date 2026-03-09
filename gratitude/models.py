from django.db import models


class SourceOfGratitude(models.Model):
    text = models.TextField()

    class Meta:
        verbose_name = "Source of Gratitude"
        verbose_name_plural = "Sources of Gratitude"

    def __str__(self):
        return self.text[:60]
