from django import forms
from django.conf import settings
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV3


class ContactForm(forms.Form):
    name = forms.CharField(label='Name', widget=forms.TextInput(attrs={
        'class': 'form-control my-1', 'placeholder': 'Your name *', 'autocomplete': 'off', 'maxlength': '15'}))
    sender = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={
        'class': 'form-control my-1', 'placeholder': 'Your email *', 'autocomplete': 'off'}))
    subject = forms.CharField(label='Topic', widget=forms.TextInput(attrs={
        'class': 'form-control my-1', 'placeholder': 'Message topic *', 'autocomplete': 'off', 'maxlength': '30'}))
    content = forms.CharField(label='Text', widget=forms.Textarea(attrs={
        'class': 'form-control my-1', 'placeholder': 'Message text *', 'autocomplete': 'off', 'rows': 10}), min_length=50)
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
