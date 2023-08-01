from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from smtplib import SMTPException
from .forms import ContactForm
import re


def contains_link(text):
    url_pattern = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
    return bool(re.search(url_pattern, text))


def send(request):
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            body = {
                'name': form.cleaned_data['name'],
                'sender': form.cleaned_data['sender'],
                'content': form.cleaned_data['content'],
            }
            if contains_link(body['content']):
                messages.warning(
                    request, "Links aren't allowed in the message text!")
                return redirect('/#contacts')
            html_content = render_to_string('email.html', {
                                            'name': body['name'], 'sender': body['sender'], 'content': body['content']})
            text_content = strip_tags(html_content)
            try:
                email = EmailMultiAlternatives(
                    form.cleaned_data['subject'],
                    text_content,
                    settings.EMAIL_HOST_USER,
                    ['forvest@inbox.lv']
                )
                email.attach_alternative(html_content, 'text/html')
                email.send()
                messages.success(request, 'Message sent')
                return redirect('/#contacts')
            except SMTPException:
                messages.error(
                    request, 'Something went wrong, please, try again')
                return redirect('/#contacts')
        else:
            messages.warning(
                request, "Google thinks that you're not a human, please try again")
            return redirect('/#contacts')
    else:
        form = ContactForm()
    return render(request, 'index.html', {"form": form})
