# admin.py permet de configurer les vues dans l'administration de django
# Code réalisé par Wallywon, tout droit réservé 

#import de admin permet de configurer l'interface admin fournie par django
from django.contrib import admin
#import des models 
from backoffice.models import Author, Publisher, Book, BookAuthor, Reservation

#config pour qu'on ne voit que aut_author et aut_year_born ( ce dernier en read only)
class AuthorAdmin(admin.ModelAdmin):
    list_display=('aut_author','aut_year_born')
    read_only=('aut_year_born')

#config pour qu'on ne voit que le nom de la compagnie et son adresse(ce dernier en read only)
class PublisherAdmin(admin.ModelAdmin):
    list_display=('pub_company_name','pub_address')
    read_only=('pub_address')
    
#config pour qu'on ne voit que le nom du livre et son id(ce dernier en read only)
class BookAdmin(admin.ModelAdmin):
    list_display=('book_name','book_type')
    read_only=('book_type')
    
#config pour qu'on ne voit que le livre et le nom du user(ce dernier en read only)
class RservationAdmin(admin.ModelAdmin):
    list_display=('reservation_book','reservation_user')
    read_only=('reservation_user')
    
#config pour qu'on ne voit le livre et l'écrivain(ce dernier en read only)
class BookAuthorAdmin(admin.ModelAdmin):
    list_display=('BookAuthor_book','BookAuthor_author')
    read_only=('BookAuthor_author')

#Envoie la config dans admin( en fonction du model et de la class qu'on lui associe)   
admin.site.register(BookAuthor,BookAuthorAdmin) 
admin.site.register(Reservation,RservationAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Book,BookAdmin)
