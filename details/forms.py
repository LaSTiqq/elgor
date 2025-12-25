from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label='Name', widget=forms.TextInput(attrs={
        'id': 'name', 'class': 'form-control my-2', 'placeholder': 'Name', 'autocomplete': 'off', 'maxlength': '15'}),
        min_length=3)
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={
        'id': 'email', 'class': 'form-control my-2', 'placeholder': 'Email', 'autocomplete': 'off'}))
    subject = forms.CharField(label='Subject', widget=forms.TextInput(attrs={
        'id': 'subject', 'class': 'form-control my-2', 'placeholder': 'Subject', 'autocomplete': 'off', 'maxlength': '30'}),
        min_length=5)
    message = forms.CharField(label='Message', widget=forms.Textarea(attrs={
        'id': 'message', 'class': 'form-control my-2', 'placeholder': 'Message', 'autocomplete': 'off'}),
        min_length=20)
