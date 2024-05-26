from django import forms
from django.contrib.auth.models import User


class DeleteAccountForm(forms.Form):
    delete_confirm = forms.BooleanField(widget=forms.CheckboxInput(), 
                    label='Confirm deletion')

    class Meta:
        # This is the association between the model and the model form
        model = User