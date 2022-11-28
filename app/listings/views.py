from django.http import HttpResponse
from django.shortcuts import render, redirect
from listings.models import Ticket, Review, UserFollows
from listings.forms import LogInForm, TicketForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required


def login_page(request):
    form = LogInForm()
    message = ''
    if request.method == "POST":
        form = LogInForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password'],
            )
            if user is not None: 
                login(request, user)
                return redirect('posts')
            else: 
                message = 'Mauvais identifiants.'
    return render(
        request, 'listings/browsing/login.html', context={'form': form, 'message': message})


def logout_user(request):   
    logout(request)
    return redirect('login')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else: 
        form = UserCreationForm()
    return render (request, 'listings/browsing/register.html', {'form': form})
    

@login_required
def home(request):
    return render (request, 'listings/browsing/feed.html')


@login_required
def subscribers(request):
    return render (request, 'listings/browsing/subs.html')


@login_required
def create_ticket(request):
    if request.method =='POST':
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save()
            return redirect ('ticket-detail', ticket.id)
    else: 
        form = TicketForm()
    return render (request, 'listings/elements/newTicket.html', {'form': form})


@login_required
def create_response_critic(request):
    return render (request, 'listings/elements/critic.html')


@login_required
def create_new_critic(request):
    return render (request, 'listings/elements/newCritic.html')


@login_required
def ticket_details(request, id):
    ticket = Ticket.objects.get(id=id)
    return render(request, 'listings/elements/ticketDetails.html', {'ticket': ticket})

@login_required
def post(request):
    tickets = Ticket.objects.all()
    return render (request, 'listings/browsing/posts.html', {'tickets': tickets})


@login_required
def critic_update(request):
    return render (request, 'listings/elements/modCritic.html')


@login_required
def ticket_update(request, id):
    ticket = Ticket.objects.get(id=id)
    if request.method == 'POST':
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect ('ticket-detail', ticket.id)
    else:
        form = TicketForm(instance=ticket)
    return render (request, 'listings/elements/modTicket.html', {'form': form})