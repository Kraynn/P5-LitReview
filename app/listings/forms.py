from django import forms
from listings.models import Ticket

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = '__all__'
        #exclude = ('user',)

class LogInForm(forms.Form):
    username = forms.CharField(max_length=60, label="Nom d'utilisateur")
    password = forms.CharField(max_length=60, widget=forms.PasswordInput, label="Mot de passe")