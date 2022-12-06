from django import forms
from listings.models import Ticket, Review, UserFollows

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = '__all__'
        exclude = ('user',)


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'headline', 'body']


class LogInForm(forms.Form):
    username = forms.CharField(max_length=60, label="Nom d'utilisateur")
    password = forms.CharField(max_length=60, widget=forms.PasswordInput, label="Mot de passe")


class UserFollowsForm(forms.ModelForm):
    class Meta: 
        model = UserFollows
        fields = ['followed_user']
        labels = {"followed_user": "Liste des utilisateurs"}
