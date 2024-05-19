from django import forms
from order.models import Order

STATE = (("Not Started", "Not Started"), ("In progress", "in progress"),
         ("Finished", "finished"))

class Cancel(forms.Form):
    cancel_reason = forms.CharField(label="Cancel reason", max_length=200)

    class Meta:
        fields = ('cancel_reason',)
        #This is the association between the model and the model form
        model = Order


class ChangeStatus(forms.Form):
    state = forms.ChoiceField(widget=forms.RadioSelect(attrs={"class" : "my-2"}), 
                              choices=STATE, label='')

    class Meta:
        fields = ('state',)
        #This is the association between the model and the model form
        model = Order
