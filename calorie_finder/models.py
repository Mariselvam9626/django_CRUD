from django.db import models

class Food(models.Model):

    food_name = models.CharField(max_length=100)
    calories = models.FloatField()
    protein_g = models.FloatField()
    fat_total_g = models.FloatField()

    def __str__(self):
        return self.food_name