from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),

    path('cinemas/list', views.cinemas, name='cinemas'),
    path('cinemas/<int:id_cinema>', views.cinema, name='cinema'),

    path('films/list', views.films, name='films'),
    path('films/<int:id_film>', views.film, name='film'),

    path('compte/', views.compte, name='user_account'),
    path('user_register/', views.enregistrement, name='user_register'),
    path('user_login/', views.connexion, name='user_login'),
    path('user_logout/', views.deconnexion, name = 'user_logout'),

    path('like/<str:toLike>-<int:uid>', views.like, name='like'),
    path('unlike/<str:toLike>-<int:uid>', views.unlike, name='unlike'),
]
