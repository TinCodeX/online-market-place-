from django import forms
from .models import Item

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'
class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image',)
        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES,
            }),
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Name of the item',
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Describe your item',
                
            }),
            'price': forms.NumberInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Price in Birr',
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border'
            }),
        } 