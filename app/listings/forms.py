from django import forms
from listings.models import Ticket

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = '__all__'
        #exclude = ('user',)