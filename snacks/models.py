from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Snack(models.Model):
    name = models.CharField(max_length=255,help_text="name of the snacks")
    description = models.TextField(max_length=255,help_text="Description of the snack",default="no description available")
    purchaser = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)

    def __str__(self):
        return self.name


