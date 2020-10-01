from django import forms
from shop.models import Review


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ['author', 'body', 'rating']
        widgets = {
            'rating': forms.RadioSelect(),
        }
