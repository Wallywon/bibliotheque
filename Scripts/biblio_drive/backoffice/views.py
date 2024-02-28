# views.py permet de configurer mes différentes vues 
# Code réalisé par Wallywon, tout droit réservé 

#---------------- Imports -----------------

#import de mes models 

from backoffice.models import Author
from backoffice.models import Book
from backoffice.models import Publisher
from .models import Reservation

#import pour gestion des user
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegistrationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth import logout

#render : Rend une page html en utilisant un modele django avec des données spécifiques
#redirect : Redirige la personne vers une autre URL en générant une réponse de redirection HTML
from django.shortcuts import render, redirect

#récupère un objet de la bdd et renvoie une erreur 404 si pas trouvé
from django.shortcuts import get_object_or_404


#---------------- Auteurs -----------------

#permet de lister tous les autheurs
def listAuthor(request):
    auteurs = Author.objects.all()
    return render(request, 'listAuthor.html', {'auteurs': auteurs})

#me permet d'envoyer dans authorDetail toutes les informations sur l'autheur dont l'id est dans l'url 
def author_detail(request, aut_id):
    author = Author.objects.get(pk=aut_id)
    return render(request, template_name='authorDetail.html', context={'author': author})


#---------------- Livres -----------------

#permet d'afficher la liste des livres sur Livre.html
def livre_liste(request):
    livres = Book.objects.all().order_by('book_name')
    return render(request, 'Livre.html', {'livres': livres})

#permet d'afficher les détails d'un livre + si verifie si le user actuel(si connecté) l'a déjà reservé 
# (présence d'une relation dans la table Reservation) et renvoie true or false + les infos du livre
def detail_livre(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    is_book_reserved = False
    
    if request.user.is_authenticated:
        reservation = request.user.reservation_set.filter(reservation_book=book).first()
        is_book_reserved = reservation is not None

    return render(request, 'detail_livre.html', {'book': book, 'is_book_reserved': is_book_reserved})


#---------------- Editeurs -----------------

#Permet d'aficher la liste des éditeurs dans listEditeur.html
def listEditeur(request):
    editeurs = Publisher.objects.all()
    return render(request, 'listEditeur.html', {'editeurs': editeurs})

#permet d'afficher le détail d'un éditeur en particulier
def detail_editeur(request, pub_id):
    editeur = Publisher.objects.get(pk=pub_id)
    livres_editeur = Book.objects.filter(book_publisher=editeur)
    return render(request, template_name='detail_editeur.html', context={'editeur': editeur, 'livres_editeur': livres_editeur})


#---------------- Réservation -----------------

# permet d'emprunter un livre si un user est connecté
def reserver_livre(request, book_id):
    if request.user.is_authenticated:
        user = request.user
        book = get_object_or_404(Book, pk=book_id)

        # Vérifier si une réservation existe déjà pour ce user et ce livren (existing_reservation est un boolean)
        existing_reservation = Reservation.objects.filter(reservation_user=user, reservation_book=book).first()

        # Si une réservation existe et que la quantité est > 0 alors reservation
        if not existing_reservation and book.book_quantite > 0:
            book.book_quantite -= 1
            book.save()
            requestuser = User.objects.get(pk=user.id)
            reservation = Reservation()
            reservation.reservation_book = book
            reservation.reservation_user = requestuser
            reservation.save()

        return redirect('detail_livre', book_id=book_id)

# permet de rendre un livre. Comme je n'ai pas défini de quantité "total" et de quantité "en stock" j'ai défini que je pouvais
# avoir 10 exemplaires max de chaque livres . 
def rendre_livre(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    # Vérifier si une réservation existe pour ce user et ce livre (reservation est un boolean)
    reservation = Reservation.objects.filter(reservation_user=request.user, reservation_book=book).first()
    
    #Si une reservation en cours alors quantité -1 et supression de la reservation
    if reservation:
        if book.book_quantite < 10:
            book.book_quantite += 1
            book.save()
        reservation.delete()

    return redirect('detail_livre', book_id=book_id)


#---------------- Rediréctions -----------------

#me permet la redirection vers ma page d'accueil 
def home1(request):
    return render(request, 'home1.html')


#---------------- Login Logout et Création user -----------------

#permet de log un user, utilisé sur login.html
def user_login(request):
    #utilisation de la methode POST
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                print("User authenticated:", user) 
                return redirect('hom1')  # redirige vers home1 (ma page d'accueil)
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

#Permet de me logout puis redirige vers home (ma page d'accueil)
def user_logout(request):
    logout(request)
    return redirect('home1') 

#Permet de créer un nouveau user et le connecte directement 
def user_registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('hom1') 
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/user_registration.html', {'form': form})