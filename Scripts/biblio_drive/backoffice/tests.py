# tests.py permet de réaliser mes tests 
# Code réalisé par Wallywon, tout droit réservé 

from django.test import TestCase
from django.urls import resolve, reverse, Resolver404
from backoffice.views import home1
from .models import Author, Publisher, Book

class ModelTests(TestCase):
    #création d'un environnement de test pour autheur et éditeur 
    def setUp(self):
        self.author = Author.objects.create(aut_author='John Doe', aut_year_born=1980)
        self.publisher = Publisher.objects.create(pub_name='test nom', pub_company_name=' test company nom', pub_address='test adresse' )
        self.book = Book.objects.create(book_name='test nom du livre',book_quantite='test quantité du livre' )

    
    #test si l'url home fonctionne, si elle n'est pas trouvé alors renvoyer une erreur
    def test_url(self):
        try:
            found = resolve('/home')
            self.assertEqual(found.func,home1)
        except Resolver404:
            self.fail()
    
    #test si le nom de l'éditeur défini en setUp ont bien été implémentés dans la bdd (dans le test)
    def test_publisher_str(self):
        self.assertEqual(str(self.publisher),'test nom')
        
    #test si les détails de l'auteur défini en setUp ont bien été implémentés dans la bdd (dans le test)
    def test_author_detail_view(self):
        response = self.client.get(reverse('author-detail', args=[self.author.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authorDetail.html')
        self.assertContains(response, 'Détails de l\'Auteur')
        self.assertContains(response, 'John Doe')
    
    #test si le nom du livre défini en setUp a bien été implémentés dans la bdd (dans le test)
    def test_book_str(self):
        self.assertEqual(str(self.book),'test nom du livre')
    