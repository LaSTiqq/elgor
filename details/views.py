from django.views.decorators.http import require_POST, require_GET
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from smtplib import SMTPException
from .forms import ContactForm
from .utils import restricted_found
import requests
import re


@require_GET
def home(request):
    form = ContactForm()
    return render(request, 'index.html', {'form': form})


@require_POST
def send_ajax(request):
    form = ContactForm(data=request.POST)
    if form.is_valid():
        if any(restricted_found(form.cleaned_data[field]) for field in ['name', 'subject', 'message']):
            return JsonResponse({
                "status": "warning",
                "message": "You wrote something disallowed! Please try again."
            }, status=400)

        recaptcha_response = request.POST.get('g-recaptcha-response')
        secret_key = settings.RECAPTCHA_PRIVATE_KEY
        verification_url = "https://www.google.com/recaptcha/api/siteverify"
        response = requests.post(verification_url, data={
            'secret': secret_key,
            'response': recaptcha_response
        })
        result = response.json()

        if not result.get('success') or result.get('score', 0) < settings.RECAPTCHA_REQUIRED_SCORE:
            return JsonResponse({
                "status": "warning",
                "message": "Captcha verification failed. Please try again."
            }, status=400)

        html_content = render_to_string("email.html", {
            'name': form.cleaned_data['name'],
            'email': form.cleaned_data['email'],
            'message': form.cleaned_data['message']
        })
        text_content = re.sub(r"<[^>]+>", "", html_content)

        try:
            email = EmailMultiAlternatives(
                form.cleaned_data['subject'],
                text_content,
                settings.EMAIL_HOST_USER,
                ['forvest@inbox.lv']
            )
            email.attach_alternative(html_content, "text/html")
            email.send()
            return JsonResponse({
                "status": "success",
                "message": "Message sent!"
            })
        except SMTPException:
            return JsonResponse({
                "status": "danger",
                "message": "Something went wrong! Please try again."
            }, status=500)
