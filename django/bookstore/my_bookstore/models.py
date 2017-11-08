from django.db import models
import datetime

class Book(models.Model):
    GENRE_CHOICES = (
        ('H', 'History'),
        ('C', 'Classic'),
        ('F', 'Fiction'),
        ('NF', 'Non-fiction'),
        ('M', 'Mystery'),
    )

    title = models.CharField(max_length=80)
    price = models.FloatField()
    genre = models.CharField(max_length=200, choices=GENRE_CHOICES)
    description = models.TextField(blank=True)
    pages = models.IntegerField()
    published = models.DateField()
    cover = models.ImageField(upload_to="cover_imgs", blank=True)

    def __str__(self):
        return self.title