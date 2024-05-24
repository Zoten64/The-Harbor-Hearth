from django import forms
from order.models import Order
from contact.models import ContactModel

STATE = (("NOT-STARTED", "Not Started"), ("IN-PROGRESS", "In Progress"),
         ("FINISHED", "Finished"))


class Cancel(forms.Form):
    cancel_reason = forms.CharField(widget=forms.TextInput(
        attrs={"class": "field_text_input"}), label="Cancel reason", 
        max_length=200)

    class Meta:
        # This is the association between the model and the model form
        model = Order


class ChangeStatus(forms.Form):
    state = forms.ChoiceField(widget=forms.RadioSelect(attrs={"class": "my-2"}),
                              choices=STATE, label='')

    class Meta:
        # This is the association between the model and the model form
        model = Order

class DeleteOrder(forms.Form):
    delete_confirm = forms.BooleanField(widget=forms.CheckboxInput(), 
                    label='Confirm deletion')

    class Meta:
        # This is the association between the model and the model form
        model = Order

class ContactResponse(forms.Form):
    employee_response = forms.CharField(widget=forms.TextInput(
        attrs={"class": "field_text_input"}), max_length=1500 ,label="")
    class Meta:
        # This is the association between the model and the model form
        model = ContactModel
