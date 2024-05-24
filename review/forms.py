from django import forms
from .models import Review

RATING = ((1, "1 star"), (2, "2 stars"), (3, "3 stars"), 
          (4, "4 stars"), (5, "5 stars"))

class ReviewForm(forms.Form):
    rating = forms.ChoiceField(choices=RATING)
    title = forms.CharField(widget=forms.TextInput(
        attrs={"class": "field_text_input"}))
    content = forms.CharField(widget=forms.TextInput(
        attrs={"class": "field_text_input"}), max_length=1500)
    
    class Meta:
        model = Review