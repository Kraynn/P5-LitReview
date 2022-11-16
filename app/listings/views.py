from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Ticket

def login(request):
    return render (request, 'listings/browsing/login.html')

def register(request):
    return render (request, 'listings/browsing/register.html')
    
def home(request):
    return render (request, 'listings/browsing/feed.html')

def subscribers(request):
    return render (request, 'listings/browsing/subs.html')

def create_ticket(request):
    return render (request, 'listings/elements/newTicket.html')

def create_response_critic(request):
    return render (request, 'listings/elements/critic.html')

def create_new_critic(request):
    return render (request, 'listings/elements/newCritic.html')

def post(request):
    tickets = Ticket.objects.all()
    return render (request, 'listings/browsing/posts.html', {'tickets': tickets})

def modify_critic(request):
    return render (request, 'listings/elements/modCritic.html')

def modify_ticket(request):
    return render (request, 'listings/elements/modTicket.html')