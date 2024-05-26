"""Employee only forms"""
from django import forms
from order.models import Order
from contact.models import ContactModel

STATE = (("Not Started", "Not Started"), ("In Progress", "In Progress"),
         ("Finished", "Finished"))


class Cancel(forms.Form):
    """Form for cancelling orders"""
    cancel_reason = forms.CharField(widget=forms.TextInput(
        attrs={"class": "field_text_input"}), label="Cancel reason",
        max_length=200)

    class Meta:
        # This is the association between the model and the model form
        model = Order


class ChangeStatus(forms.Form):
    """Form for changing order status"""
    state = forms.ChoiceField(widget=forms.RadioSelect(attrs={"class": "my-2"}),
                              choices=STATE, label='')

    class Meta:
        # This is the association between the model and the model form
        model = Order

class DeleteOrder(forms.Form):
    """Form for deleting orders"""
    delete_confirm = forms.BooleanField(widget=forms.CheckboxInput(),
                    label='Confirm deletion')

    class Meta:
        # This is the association between the model and the model form
        model = Order

class ContactResponse(forms.Form):
    """Response to customer contact forms"""
    employee_response = forms.CharField(widget=forms.Textarea(
        attrs={"class": "field_text_input"}), max_length=1500 ,label="")
    class Meta:
        # This is the association between the model and the model form
        model = ContactModel
