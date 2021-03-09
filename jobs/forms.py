from django import forms

class filterJob(forms.Form):
    search = forms.CharField(max_length=200)

