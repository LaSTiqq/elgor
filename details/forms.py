from django import forms
from django.conf import settings
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV3


class ContactForm(forms.Form):
    name = forms.CharField(label='Name', widget=forms.TextInput(attrs={
                           'class': 'form-control my-1', 'placeholder': 'Your name *', 'autocomplete': 'off', 'required': True}))
    sender = forms.EmailField(label='Email', widget=forms.EmailInput(
        attrs={'class': 'form-control my-1', 'placeholder': 'Your email *', 'autocomplete': 'off', 'required': True}))
    subject = forms.CharField(label='Topic', widget=forms.TextInput(
        attrs={'class': 'form-control my-1', 'placeholder': 'Message topic *', 'autocomplete': 'off', 'required': True}))
    content = forms.CharField(label='Text', widget=forms.Textarea(
        attrs={'class': 'form-control my-1', 'rows': 10, 'placeholder': 'Message text *', 'autocomplete': 'off', 'required': True}))
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
