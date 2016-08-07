from django.db import models

class Portfolio(models.Model):
    grid_image = models.ImageField()
    grid_title = models.CharField(max_length=100)
    grid_detail = models.CharField(max_length=100)

    modal_title = models.CharField(max_length=100)
    modal_subtitle = models.CharField(max_length=100)
    modal_image = models.ImageField()
    modal_detail = models.TextField()
