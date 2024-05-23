from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
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

            msg = f"Hello {name}! Thank you for contacting us." \
            "Here's what you wrote: \n" \
            f"{message} \n" \
            "Please be patient for an answer. \n" \
            "Sincerely, The Harbour Hearth Team"
            send_mail(
                "We've recieved your contact form",
                msg,
                None,
                [email],
                fail_silently=False,
            )
            messages.success(request, 'Message sent')
    form = ContactForm
    context = {"form" : form}
    return render(request, 'contact/contact.html', context)