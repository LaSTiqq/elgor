from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from smtplib import SMTPException
from .forms import ContactForm
import re


def restricted_found(text):
    url_pattern = re.compile(
        r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    restricted_keywords = ["whatsapp", "telegram", "tg", "телеграм", "телега", "тг",
                           "viber", "вайбер", "discord", "дискорд", "аська", "icq",
                           "porn", "loli", "xxx", "cp", "skype", "скайп", "rub",
                           "рублей", "руб", "dollars", "eur", "bonus", "free",
                           "gift", "order now", "spam", "website", "visit our",
                           "earn", "congratulations", "don't miss", "buy now",
                           "limited time", "exclusive offer", "act fast", "special deal",
                           "discount", "sale", "promotion", "pharmacy", "election", "price"]

    has_link = bool(re.search(url_pattern, text))
    has_restricted_keyword = any(re.search(
        r'\b' + re.escape(keyword) + r'\b', text, flags=re.IGNORECASE) for keyword in restricted_keywords)

    return has_link or has_restricted_keyword


def send(request):
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            if any(restricted_found(form.cleaned_data[field]) for field in ['name', 'subject', 'content']):
                messages.warning(
                    request, 'You wrote something disallowed! Try again.')
                return redirect('/#contacts')
            html_content = render_to_string('email.html', {
                'name': form.cleaned_data['name'],
                'sender': form.cleaned_data['sender'],
                'content': form.cleaned_data['content']
            })
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
                messages.success(request, "Message sent")
                return redirect('/#contacts')
            except SMTPException:
                messages.error(
                    request, "Something went wrong! Try again.")
                return redirect('/#contacts')
        else:
            messages.error(
                request, "Google thinks that you're not a human! Try again.")
            return redirect('/#contacts')
    else:
        form = ContactForm()
    return render(request, 'index.html', {"form": form})
