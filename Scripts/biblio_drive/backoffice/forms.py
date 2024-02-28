# forms.py permet de gérer les formulaires
# Code réalisé par Wallywon, tout droit réservé 

#import du forms de django qui fourni les classes pour la création de formulaire
from django import forms
#import de UserCreationForms qui est un formulaire fourni par django
from django.contrib.auth.forms import UserCreationForm
#import de User qui est le modèle d'utilisateur fourni par Django
from django.contrib.auth.models import User

# UserRegistrationForm hérite des fonctionnalités de UserCreationForms
class UserRegistrationForm(UserCreationForm):
    #configuration des metadonnées du formulaire 
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
