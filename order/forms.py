from django import forms
from .models import Order

DELIVERY_METHOD = (("Eat-in: Counter", "EAT-IN-COUNTER"), 
                   ("Eat-in: Table delivery", "EAT-IN-TABLE"), 
                   ("Take-Out", "TAKE-OUT"))

# if the user is not logged in they will need to enter their email
class OrderEmail(forms.Form):
    email = forms.EmailField()

    class Meta:
        fields = ('email',)
        # This is the association between the model and the model form
        model = Order
    
class OrderForm(forms.Form):
    order = forms.Textarea()
    delivery_method = forms.ChoiceField(choices=DELIVERY_METHOD)

    class Meta:
        fields = ('order', 'delivery_method')
        # This is the association between the model and the model form
        model = Order