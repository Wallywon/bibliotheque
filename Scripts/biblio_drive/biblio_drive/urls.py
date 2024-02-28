"""
URL configuration for biblio_drive project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from backoffice import views
from django.conf import settings
from django.conf.urls import include 
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from backoffice.views import user_login
from backoffice.views import user_login, user_registration
from backoffice.views import user_logout
from django.contrib.auth.views import LoginView

urlpatterns=[
    path('admin/',admin.site.urls),
    path('home1', views.home1, name='home1'),                                       #Accueil de notre site 
    path('listAuthor/',views.listAuthor,name="listAuthor"),                         #liste de tous les auteurs (cliquable pour plus de détails)
    path('author-detail/<int:aut_id>/', views.author_detail, name='author_detail'), # donne les détais d'un auteurs en fonction de son id
    path('livre_liste/',views.livre_liste,name="livre_liste"),                      # liste tous les livres en cliquable pour donner plus de détails 
    path('detail_livre/<int:book_id>',views.detail_livre,name="detail_livre"),      # donne les détails d'un livre en fonction de son id
    path('reserver_livre/<int:book_id>/', views.reserver_livre, name='reserver_livre'), # page fantome pour réserver depuis détails livre
    path('rendre_livre/<int:book_id>/', views.rendre_livre, name='rendre_livre'),       # page fantome pour rendre un livre depuis détails livre 
    path('listEditeur/',views.listEditeur,name="listEditeur"),                      # liste tous les livres en cliquable pour donner plus de détails 
    path('detail_editeur/<int:pub_id>',views.detail_editeur,name="detail_editeur"),      # donne les détails d'un livre en fonction de son id
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('login/', user_login, name='login'),
    path('user_registration/', user_registration, name='user_registration'),
    path('logout/', user_logout, name='logout'),   # path('listing2/',views.listing2,name="listing2"),  
    #   path('listing/',views.listing,name="listing"),
    path('login/', LoginView.as_view(), name='login'),


]
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
