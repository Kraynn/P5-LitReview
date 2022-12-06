from django.http import HttpResponse
from django.shortcuts import render, redirect
from listings.models import Ticket, Review, UserFollows
from listings.forms import LogInForm, TicketForm, UserFollowsForm, ReviewForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from itertools import chain
from django.db.models import CharField, Value
from django.db.models import Q


"""
Views for browsing and account managing purposes
"""

def login_user(request):
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
        request, 'listings/browsing/login.html',
        context={'form': form, 'message': message})


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
def subscribe(request): 
    followers = UserFollows.objects.filter()
    if request.method == 'POST':
        form = UserFollowsForm(request.POST)
        if form.is_valid():
            sub = form.save(commit=False)
            sub.user = request.user
            sub.save()
            return redirect('sub')
    else:
        form = UserFollowsForm()
        subs = UserFollows.objects.filter(user=request.user)
    return render (request,'listings/browsing/subs.html',
    context = {'form': form, 'subs': subs})

@login_required    
def unsubscribe(request, id_user):
    if request.method == 'POST':
        relation = UserFollows.objects.get(
        user=request.user, followed_user=id_user)
        if relation: 
            relation.delete()
    return redirect('sub')

def get_followed_users(user):
    user_follows_objects = user.following.all()
    return [
        user_follows_object.followed_user
        for user_follows_object in user_follows_objects
    ]

def get_users_viewable_tickets(user):
    followed_users = get_followed_users(user)
    return Ticket.objects.filter(
        Q(user__in=followed_users) | Q(user=user)
    )

def get_users_viewable_reviews(user):
    followed_users = get_followed_users(user)
    return Review.objects.filter(
        Q(user__in=followed_users) | Q(user=user) | Q(ticket__user=user)
        )

@login_required
def home(request):
    reviews = get_users_viewable_reviews(request.user)
    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))
    tickets = get_users_viewable_tickets(request.user) 
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))
    posts = sorted(
        chain(reviews, tickets), 
        key=lambda post: post.time_created, 
        reverse=True
    )
    return render(request, 'listings/browsing/feed.html', context={'posts': posts})


@login_required
def post(request):
    tickets = Ticket.objects.all()
    return render (request, 'listings/browsing/posts.html',
    {'tickets': tickets})


""" 
Views for element creation purposes
TICKETS
"""

@login_required
def create_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save()
            return redirect ('ticket-detail', ticket.id)
    else: 
        form = TicketForm()
    return render (request, 'listings/elements/newTicket.html',
    {'form': form})

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
    return render (request, 'listings/elements/modTicket.html',
    {'form': form})

@login_required
def ticket_details(request, id):
    ticket = Ticket.objects.get(id=id)
    return render(request, 'listings/elements/ticketDetails.html',
    {'ticket': ticket})

@login_required
def ticket_delete(request, id):
    if request.method == "POST":
        ticket = Ticket.objects.get(id=id)
        if ticket:
            ticket.delete()
            return redirect('posts')


"""
REVIEWS
"""

@login_required
def create_ticket_review(request, ticket_id):
    ticket = Ticket.objects.get(pk=ticket_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.ticket = ticket
            review.user = request.user 
            review.save()
            return redirect('home')
    else:
        review_form = ReviewForm()
    return render (request, 'listings/elements/newReview',
    context = {'ticket': ticket, 'form': review_form})
        
@login_required
def create_review(request):
    ticket_form = TicketForm(request.POST, request.FILES)
    review_form = ReviewForm(request.POST)
    if request.method == 'POST':
        if all([ticket_form.is_valid(), review_form.is_valid()]):
            ticket_form.instance.user = request.user
            ticket = ticket_form.save()
            review_form.instance.user = request.user
            review_form.instance.ticket = Ticket.objects.get(pk=ticket.pk)
            review_form.save()
            return redirect ('posts')       
    return render (request, 'listings/elements/review.html',
    context = {'ticketform': ticket_form, 'reviewform': review_form})

@login_required
def review_update(request, review_id):
    review = Review.objects.get(pk=review_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.ticket = Ticket.objects.get(pk=review.ticket.id)
            review.save()
            return redirect('posts')
    else:
        form= ReviewForm(instance=review)
    return render(request, 'listings/elements/modReview', {'form': form})    

@login_required
def review_delete(request, id):
    if request.method == "POST":
        review = Review.objects.get(id=id)
        if review:
            review.delete()
            return redirect('posts')

def testview(request):
    followers = UserFollows.objects.filter(followed_user=request.user)
    return render (request, 'listings/test.html', {'followers': followers})