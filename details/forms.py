from django import forms
from django.conf import settings


class ContactForm(forms.Form):
    name = forms.CharField(label='Name', widget=forms.TextInput(attrs={
        'id': 'name', 'value': 'John', 'class': 'form-control', 'placeholder': 'Name', 'autocomplete': 'off', 'maxlength': '15'}),
        min_length=3)
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={
        'id': 'email', 'value': 'john.doe@gmail.com', 'class': 'form-control', 'placeholder': 'Email', 'autocomplete': 'off'}))
    subject = forms.CharField(label='Subject', widget=forms.TextInput(attrs={
        'id': 'subject', 'value': 'Collaboration', 'class': 'form-control', 'placeholder': 'Subject', 'autocomplete': 'off', 'maxlength': '30'}),
        min_length=5)
    message = forms.CharField(label='Message', widget=forms.Textarea(attrs={
        'id': 'message', 'class': 'form-control', 'placeholder': 'Message', 'autocomplete': 'off'}),
        min_length=20)
