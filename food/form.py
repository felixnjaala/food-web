from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields =['item_name', 'item_desc', 'item_price', 'item_image']


class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False, label='Search')        