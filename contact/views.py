"""Contact views"""
from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from .models import ContactModel
from .forms import ContactForm


# Create your views here.

def contact_view(request):
    """View for submitting a contact form"""
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            #Clean the data and put into variables
            name = contact_form.cleaned_data['name']
            email = contact_form.cleaned_data['email']
            phone_number = contact_form.cleaned_data['phone_number']
            preferred_contact = contact_form.cleaned_data['preferred_contact']
            message = contact_form.cleaned_data['message']

            #Create the object and add it to the database
            ContactModel.objects.create(
                name = name,
                email = email,
                phone_number = phone_number,
                preferred_contact = preferred_contact,
                message = message,
            )

            #The email that will be sent upon form submission
            msg = f"Hello {name}! Thank you for contacting us." \
            "Here's what you wrote: \n" \
            f"{message} \n" \
            "Please be patient for an answer. \n" \
            "Sincerely, The Harbour Hearth Team"
            send_mail(
                "We've recieved your message",
                msg,
                None,
                [email],
                fail_silently=False,
            )
            messages.success(request, 'Message sent')
    form = ContactForm
    context = {"form" : form}
    return render(request, 'contact/contact.html', context)
