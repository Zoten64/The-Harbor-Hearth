from django import forms
from .models import ContactModel

PREFERRED_CONTACT = (("PHONE", "phone"),("EMAIL", "E-mail"))

class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(
        attrs={"class": "field_text_input"}), label="Full Name")
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={"class": "field_text_input"}))
    #Phone number consists of 9-10 digits
    phone_number = forms.CharField(widget=forms.TextInput(
        attrs={"class": "field_text_input"}), min_length=9, max_length=10)
    preferred_contact = forms.ChoiceField(widget=forms.RadioSelect(
        attrs={"class": "my-2 border-solid"}), choices=PREFERRED_CONTACT, 
        label='Which contact method would you prefer we use?')
    message = forms.CharField(widget=forms.Textarea(
        attrs={"class": "field_text_input"}), max_length=1500)

    class Meta:
        model = ContactModel