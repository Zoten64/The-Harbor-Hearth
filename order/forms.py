"""Order forms"""
from django import forms
from .models import Order

DELIVERY_METHOD = (("COUNTER", "Eat-in: Pick up at counter"),
                   ("TABLE", "Eat-in: Table delivery"),
                   ("TAKE-OUT", "Take-Out"))

class OrderEmail(forms.Form):
    """Separate form for email. It shows up if the user is not logged in"""
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={"class": "field_text_input"}))

    class Meta:
        model = Order

class OrderForm(forms.Form):
    """This is the form that shows up on the order page"""
    #Hide this later as this will be handled with javascript
    order_info = forms.CharField(widget=forms.Textarea(
        attrs={"class": "field_text_input"}))
    delivery_method = forms.ChoiceField(widget=forms.RadioSelect(
        attrs={"class": "my-2 border-solid"}), choices=DELIVERY_METHOD,
        label='')
    #This field will be hidden by default. Using javascript this will be
    #shown if the table delivery option is selected.
    #This field will be set to required in the case above through JS
    table_number = forms.IntegerField(
        widget=forms.NumberInput(attrs={"class": "field_text_input", "style" :
        "display: none;", "placeholder" : "Table Number"}),
        min_value=1, max_value=20, required=False, label='')

    class Meta:
        model = Order
