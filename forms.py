from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(required=False, max_length=100)
    surname = forms.CharField(required=False, max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
