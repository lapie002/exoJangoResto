# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^accueil$', views.home), # Accueil du blog
    # url(r'^plat/(\d+)$', views.view_plat),  # Vue d'un plat : http://127.0.0.1:8000/gestionplats/plat/1
    # url(r'^plats/(\d{4})/(\d{2})$', views.list_plats),  # Vue des plats d'un mois précis : http://127.0.0.1:8000/gestionplats/plats/2014/10
    # url(r'^plat/(?P<id_plat>\d+)$', views.view_plat), # Vue d'un plat : http://127.0.0.1:8000/gestionplats/plat/1
    url(r'^plat/(?P<id_plat>\d+)$', views.view_plat, name="afficher_plat"), # Vue d'un plat : avec redirect
    url(r'^plats/(?P<year>\d{4})/(?P<month>\d{2})$', views.list_plats), # Vue des plats d'un mois précis : http://127.0.0.1:8000/gestionplats/plats/2014/10
    url(r'^redirection$', views.view_redirection), # pour la redirection
    url(r'^redirectgender$', views.view_redirection_sexe), # pour la redirection avec le genre d ela personne
    url(r'^date$', views.date_actuelle), # pour la vue sur la date actuelle
    url(r'^addition/(?P<nombre1>\d+)/(?P<nombre2>\d+)/$', views.addition), # pour la vue sur l addition de deux chiffres
    url(r'^arcenciel$', views.view_arc_en_ciel),
    url(r'^mapage$', views.mapage),
    url(r'^plats$', views.listerAllPlats)
]
