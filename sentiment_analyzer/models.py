from django.db import models

class EmojiAnalysis(models.Model):
    text = models.TextField()
    emoji = models.CharField(max_length=50)
    polarity = models.FloatField()

    def __str__(self):
        return self.text