from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from .models import ProductComment

PAYMENT_OPTION = (
    ('P', 'paypal'), 
    ('D', 'debit')
)

class AddressForm(forms.Form):
    shipping_address1 = forms.CharField(widget=forms.TextInput(), required=False)
    shipping_address2 = forms.CharField(widget=forms.TextInput(), required=False)
    shipping_city = forms.CharField(required=False)
    shipping_country = CountryField(blank_label='Select Country').formfield(required=False, 
    widget=CountrySelectWidget(attrs={'class': 'custom-select'}))
    shipping_zipcode = forms.CharField(widget=forms.TextInput(), required=False)
    set_default_shipping = forms.BooleanField(widget=forms.CheckboxInput(), required=False)
    use_default_shipping = forms.BooleanField(widget=forms.CheckboxInput(), required=False)
    same_billing_address = forms.BooleanField(widget=forms.CheckboxInput(), required=False)

    billing_address1 = forms.CharField(widget=forms.TextInput(), required=False)
    billing_address2 = forms.CharField(widget=forms.TextInput(), required=False)
    billing_city = forms.CharField(required=False)
    billing_country = CountryField(blank_label='Select Country').formfield(required=False, 
    widget=CountrySelectWidget(attrs={'class': 'custom-select'}))
    billing_zipcode = forms.CharField(widget=forms.TextInput(), required=False)
    set_default_billing = forms.BooleanField(widget=forms.CheckboxInput(), required=False)
    use_default_billing = forms.BooleanField(widget=forms.CheckboxInput(), required=False)

    payment_option = forms.ChoiceField(widget=forms.RadioSelect, choices=PAYMENT_OPTION)

class CommentForm(forms.ModelForm):
    class Meta:
        model = ProductComment
        fields = ('comment',)
    
    widgets = {
        'comment' : forms.Textarea(attrs ={'class': "form-control", 'rows': "2", 'placeholder': "Type in your review..."})
    }
