# models.py permet de configurer mes différents models
# Code réalisé par Wallywon, tout droit réservé 

from django.db import models
from django.contrib.auth.models import User

#Model représentant mes auteurs
class Author(models.Model):
    aut_id = models.AutoField(primary_key=True)
    aut_author = models.CharField(max_length=50)
    aut_year_born = models.SmallIntegerField()
    def __str__(self):
        return self.aut_author
    
#Model représentant mes Editeurs
class Publisher(models.Model):
    pub_id = models.AutoField(primary_key=True)
    pub_name = models.CharField(max_length=50)
    pub_company_name = models.CharField(max_length=255)
    pub_address = models.CharField(max_length=50) 
    def __str__(self):
        return self.pub_name
    
#Model représentant mes Livres
class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=255)
    book_type = models.SmallIntegerField()
    book_publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    book_quantite = models.SmallIntegerField()
    book_image = models.ImageField(upload_to='', null=True, blank=True)
    def __str__(self):
        return self.book_name

#Model représentant mes relations livre - Auteurs
class BookAuthor(models.Model):
    BookAuthor_author = models.ForeignKey(Author, on_delete=models.CASCADE)
    BookAuthor_book = models.ForeignKey(Book, on_delete=models.CASCADE)

#Model représentant mes relation livre - User 
class Reservation(models.Model):
    reservation_book = models.ForeignKey(Book, on_delete=models.CASCADE)
    reservation_user = models.ForeignKey(User, on_delete=models.CASCADE)
 