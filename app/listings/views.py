from django.http import HttpResponse
from django.shortcuts import render

def login(request):
    return HttpResponse("<h1> Accueil </h1>")

def register(request):
    return HttpResponse("<h1> S'enregistrer </h1>")
    
def home(request):
    return HttpResponse("<h1> Flux </h1>")

def subscribers(request):
    return HttpResponse("<h1> Abonnés </h1>")

def create_ticket(request):
    return HttpResponse("<h1> Créer un ticket </h1>")

def create_response_critic(request):
    return HttpResponse("<h1> Créer une critique en réponse </h1>")

def create_new_critic(request):
    return HttpResponse("<h1> Créer une critique sans réponse </h1>")

def post(request):
    return HttpResponse("<h1> Vos posts </h1>")

def modify_critic(request):
    return HttpResponse("<h1> Modifier critique </h1>")

def modify_ticket(request):
    return HttpResponse("<h1> Modifier ticket </h1>")