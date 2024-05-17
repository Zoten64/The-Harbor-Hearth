from django import forms
from order.models import Order

class Cancel(forms.Form):
    cancel_reason = forms.CharField(label="Cancel reason", max_length=200)

    class Meta:
        fields = ('cancel_reason',)
        #This is the association between the model and the model form
        model = Order