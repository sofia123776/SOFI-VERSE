from django import forms
from .models import Order


class CheckoutForm(forms.ModelForm):

    class Meta:
        model = Order

        fields = [
            'full_name',
            'email',
            'phone',
            'county',
            'town',
            'address'
        ]

        widgets = {
            'address': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control'
            })