from django.db import models
import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    avatar = models.ImageField(upload_to="user_imgs", blank=True)
    def __str__(self):
        return "{} - {}".format(self.user.username, self.id)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Author(models.Model):
    name = models.CharField(max_length=120)
    biography = models.TextField(blank=True)

    def __str__(self):
        return "{} - {}".format(self.name, self.id)
        
class Book(models.Model):

    genre_dict = { 
      "History": "H", "Classic": "C", 'Fiction': 'F',
      'Non-fiction': "NF", 'Mystery': "M", "Biography": "B",
      "Best seller": "BS"
    }
    
    GENRE_CHOICES = [(code,label) for label,code in genre_dict.items()]
    
     
    title = models.CharField(max_length=80)
    price = models.FloatField()
    genre = models.CharField(max_length=200, choices=GENRE_CHOICES)
    description = models.TextField(blank=True)
    pages = models.IntegerField()
    published = models.DateField()
    cover = models.ImageField(upload_to="cover_imgs", blank=True)
    
    author = models.ForeignKey('Author', on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return "{} - {}".format(self.title, self.id)

    def get_cat_name(self):

        for key in self.genre_dict:
            if (self.genre_dict[key] ==  self.genre):
                return key

def add_cat_names(request):
    color = request.session.get("color", "gray")
    return {"categories": Book.genre_dict.keys(), "color": color}
    
    
class Comment(models.Model):
    title = models.CharField(max_length=150, blank=True)
    body = models.TextField(blank=True)
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    user = models.ForeignKey("Profile", on_delete=models.CASCADE)
    rating = models.IntegerField(blank=True)
    
    
    
