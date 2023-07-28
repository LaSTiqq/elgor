from django import forms
# from django.conf import settings
# from captcha.fields import ReCaptchaField
# from captcha.widgets import ReCaptchaV2Checkbox


class ContactForm(forms.Form):
    name = forms.CharField(label='Your name', widget=forms.TextInput(attrs={
                           'class': 'form-control my-1', 'placeholder': 'Your name *', 'autocomplete': 'off', 'required': True}))
    sender = forms.EmailField(label='Your email', widget=forms.EmailInput(
        attrs={'class': 'form-control my-1', 'placeholder': 'Your email *', 'autocomplete': 'off', 'required': True}))
    subject = forms.CharField(label='Message topic', widget=forms.TextInput(
        attrs={'class': 'form-control my-1', 'placeholder': 'Message topic *', 'autocomplete': 'off', 'required': True}))
    content = forms.CharField(label='Message text', widget=forms.Textarea(
        attrs={'class': 'form-control my-1', 'rows': 10, 'placeholder': 'Message text *', 'autocomplete': 'off', 'required': True}))
    # captcha = ReCaptchaField(
    #     label='Captcha',
    #     widget=ReCaptchaV2Checkbox(
    #         attrs={
    #             'style': 'display: flex; justify-content: center; margin-top: 0.5rem;',
    #             'data-sitekey': settings.RECAPTCHA_PUBLIC_KEY,
    #         },
    #     ),
    # )
