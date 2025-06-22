from django import forms
from django.conf import settings
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV3


class ContactForm(forms.Form):
    name = forms.CharField(label='Name', widget=forms.TextInput(attrs={
        'id': 'name', 'value': 'John', 'class': 'form-control', 'placeholder': 'Name', 'autocomplete': 'off', 'maxlength': '15'}),
        min_length=3)
    sender = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={
        'id': 'email', 'value': 'john.doe@gmail.com', 'class': 'form-control', 'placeholder': 'Email', 'autocomplete': 'off'}))
    subject = forms.CharField(label='Topic', widget=forms.TextInput(attrs={
        'id': 'subject', 'value': 'Collaboration', 'class': 'form-control', 'placeholder': 'Topic', 'autocomplete': 'off', 'maxlength': '30'}),
        min_length=5)
    content = forms.CharField(label='Message', widget=forms.Textarea(attrs={
        'id': 'message', 'class': 'form-control', 'placeholder': 'Message', 'autocomplete': 'off'}),
        min_length=20)
    captcha = ReCaptchaField(
        label='Captcha',
        widget=ReCaptchaV3(
            attrs={
                'data-sitekey': settings.RECAPTCHA_PUBLIC_KEY,
            },
            api_params={
                'hl': 'en',
            },
        ),
    )
