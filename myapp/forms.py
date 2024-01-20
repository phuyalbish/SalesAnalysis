from django import forms

from .models import Company, Product, Sales, Client

class SignUpForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'quantity', 'c_id', 'img']



class SalesForm(forms.ModelForm):
    class Meta:
        model = Sales
        fields = ['amount', 'is_indivisual', 'p_id', 'totalprice']

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'location', 'description', 'img', 'password']
        widgets = {
            'password': forms.PasswordInput(),  # Use a password input widget for the password field
        }