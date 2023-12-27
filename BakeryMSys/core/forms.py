from django import forms


class AddOrder(forms.Form):
    customer_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control' , 'placeholder': 'Customer Name'}))
    order_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control' , 'placeholder': 'Order Name'}))
    order_quantity = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'class': 'form-control' , 'placeholder': 'Quantity'}))

class UpdateOrder(forms.Form):
    order_id = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'class':'form-control' , 'placeholder': 'Order ID'}))
    customer_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control' , 'placeholder': 'Customer Name'}))
    order_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control' , 'placeholder': 'Order Name'}))
    order_quantity = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'class': 'form-control' , 'placeholder': 'Quantity'}))

class FindOrder(forms.Form):
    order_id = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'class':'form-control' , 'placeholder': 'Order ID'}))

class LogIn(forms.Form):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class':'form-control' , 'placeholder': 'Email'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class':'form-control' , 'placeholder': 'Password'}))