
from django import forms


class NewsletterSubForm(forms.Form):
    email=forms.EmailField(max_length=500)