from django.http import HttpResponse
from django.shortcuts import render, redirect
from listings.models import Ticket, Review, UserFollows
from listings.forms import TicketForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(data= request.POST)
        if form.is_valid():
            return redirect('home')
    else: 
        form = AuthenticationForm()
    return render (request, 'listings/browsing/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else: 
        form = UserCreationForm()
    return render (request, 'listings/browsing/register.html', {'form': form})
    

def home(request):
    return render (request, 'listings/browsing/feed.html')


def subscribers(request):
    return render (request, 'listings/browsing/subs.html')


def create_ticket(request):
    if request.method =='POST':
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save()
            return redirect ('ticket-detail', ticket.id)
    else: 
        form = TicketForm()
    return render (request, 'listings/elements/newTicket.html', {'form': form})


def create_response_critic(request):
    return render (request, 'listings/elements/critic.html')


def create_new_critic(request):
    return render (request, 'listings/elements/newCritic.html')

def ticket_details(request, id):
    ticket = Ticket.objects.get(id=id)
    return render(request, 'listings/elements/ticketDetails.html', {'ticket': ticket})

def post(request):
    tickets = Ticket.objects.all()
    return render (request, 'listings/browsing/posts.html', {'tickets': tickets})


def modify_critic(request):
    return render (request, 'listings/elements/modCritic.html')


def modify_ticket(request):
    return render (request, 'listings/elements/modTicket.html')