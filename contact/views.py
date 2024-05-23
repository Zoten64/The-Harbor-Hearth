from django.shortcuts import render
from django.contrib import messages
from .models import ContactModel
from .forms import ContactForm


# Create your views here.

def ContactView(request):

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            name = contact_form.cleaned_data['name']
            email = contact_form.cleaned_data['email']
            phone_number = contact_form.cleaned_data['phone_number']
            preferred_contact = contact_form.cleaned_data['preferred_contact']
            message = contact_form.cleaned_data['message']

            new_contact_form = ContactModel.objects.create(
                name = name,
                email = email,
                phone_number = phone_number,
                preferred_contact = preferred_contact,
                message = message,
            )
            messages.success(request, 'Message sent')
    form = ContactForm
    context = {"form" : form}
    return render(request, 'contact/contact.html', context)