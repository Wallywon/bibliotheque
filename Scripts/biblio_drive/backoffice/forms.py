# forms.py permet de gérer les formulaires
# Code réalisé par Wallywon, tout droit réservé 

#import du forms de django qui fourni les classes pour la création de formulaire
from django import forms
#import de UserCreationForms qui est un formulaire fourni par django
from django.contrib.auth.forms import UserCreationForm
#import de User qui est le modèle d'utilisateur fourni par Django
from django.contrib.auth.models import User
#import de Book Author et Publisher qui sont des modèles Custo
from .models import Book, Author, Publisher

# UserRegistrationForm hérite des fonctionnalités de UserCreationForms
class UserRegistrationForm(UserCreationForm):
    #configuration des metadonnées du formulaire 
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class BookForm(forms.ModelForm):
    author = forms.ModelChoiceField(
        queryset=Author.objects.all(),
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Auteur"
    )

    class Meta:
        model = Book
        fields = ['book_name', 'book_type', 'book_publisher', 'book_quantite', 'book_image', 'author'] # Incluez 'author' si vous voulez qu'il soit traité comme les autres champs du modèle
        widgets = {
            'book_publisher': forms.Select(attrs={'class': 'form-control'}),
            'book_type': forms.NumberInput(attrs={'class': 'form-control'}),
            'book_quantite': forms.NumberInput(attrs={'class': 'form-control'}),
            'book_name': forms.TextInput(attrs={'class': 'form-control'}),
            'book_image': forms.FileInput(attrs={'class': 'form-control-file'}),
        }
