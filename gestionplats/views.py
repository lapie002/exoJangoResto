# -*- coding: utf-8 -*-

# Create your views here.
from django.http import HttpResponse, Http404
from django.shortcuts import redirect
from datetime import datetime
from django.shortcuts import render



# def home(request):
#     """ Exemple de page HTML, non valide pour que l'exemple soit concis """
#     text = u"""<h1>Bienvenue sur mon restaurant de bord de plage !</h1>
#               <p>Le restaurant ouvira ses portes bientot !</p>"""
#     return HttpResponse(text)

def home(request):
    # http://127.0.0.1:8000/gestionplats/accueil?name=bruno
    string = request.GET['name']
    return HttpResponse("Bonjour %s!" % string)

def view_redirection(request):

    return HttpResponse("Vous avez été redirigé.")


def view_plat(request, id_plat):
    """
    Vue qui affiche un plat selon son identifiant (ou ID, ici un numéro)
    Son ID est le second paramètre de la fonction (pour rappel, le premier
    paramètre est TOUJOURS la requête de l'utilisateur)
    """
    # http://127.0.0.1:8000/gestionplats/plat/1?ref=allgood

    # Si l'ID est supérieur à 100, nous considérons que l'article n'existe pas
    if int(id_plat) > 100:
        # raise Http404
        # return redirect(view_redirection)
        # return redirect(view_plat, id_plat=69)
        return redirect('afficher_plat', id_plat=69)

    string = request.GET['ref']
    text = u"""Vous avez demandé le plat #{0} ! et la reference %s!"""% string
    return HttpResponse(
    # HttpRequest.GET    -> "et le ref".request.GET['ref'].
    # "Vous avez demandé le plat #{0} ! et la reference %s!".format(id_plat) % string
    text.format(id_plat)
    )


def list_plats(request, month, year):

    # http://127.0.0.1:8000/gestionplats/plats/2014/10
    """ Liste des plats d'un mois précis. """
    return HttpResponse(
        "Vous avez demandé les plats du {0}/{1}.".format(month, year))

    # #pour page redirect vers autre url :
    # return redirect("https://www.djangoproject.com")


def date_actuelle(request):

    string = request.GET['pseudo']
    # http://127.0.0.1:8000/gestionplats/date?pseudo=bruno
    return render(request, 'gestionplats/date.html', {'pseudo':string,'date': datetime.now()})



def addition(request, nombre1, nombre2):
    #http://127.0.0.1:8000/gestionplats/addition/5/3/
    total = int(nombre1) + int(nombre2)

    # Retourne nombre1, nombre2 et la somme des deux au tpl
    return render(request, 'gestionplats/addition.html', locals())


def mapage(request):
    # http://127.0.0.1:8000/gestionplats/mapage?pseudo=bruno
    string = request.GET['pseudo']
    return render(request, 'gestionplats/mapage.html', {'pseudo':string})