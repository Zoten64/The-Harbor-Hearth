from django import forms
from .models import Review

RATING = ((1, "1 star"), (2, "2 stars"), (3, "3 stars"), 
          (4, "4 stars"), (5, "5 stars"))

class ReviewForm(forms.ModelForm):
    rating = forms.ChoiceField(widget=forms.Select(attrs={"class": "field_text_input"}) ,choices=RATING)
    title = forms.CharField(widget=forms.TextInput(
        attrs={"class": "field_text_input"}))
    content = forms.CharField(widget=forms.Textarea(
        attrs={"class": "field_text_input"}), max_length=1500)
    
    class Meta:
        model = Review
        fields = ("rating", "title", "content")

class DeleteReviewForm(forms.Form): 
    delete_confirm = forms.BooleanField(widget=forms.CheckboxInput(), 
                    label='Confirm deletion')

    class Meta:
        # This is the association between the model and the model form
        model = Review