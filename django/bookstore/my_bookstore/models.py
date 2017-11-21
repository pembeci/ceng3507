from django.db import models
import datetime

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
    return {"categories": Book.genre_dict.keys()}
    
    
    
    
    
    
