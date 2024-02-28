# apps.py permet de gérer mon app backoffice
# Code réalisé par Wallywon, tout droit réservé 

#import de la classe de configuraiton fourni par Django
from django.apps import AppConfig

# BackofficeConfig hérite de la classe AppConfig
class BackofficeConfig(AppConfig):
    #création de l'application backoffice
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'backoffice'
