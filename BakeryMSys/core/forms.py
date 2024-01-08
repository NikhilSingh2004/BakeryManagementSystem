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

    def __init__(self, *args, **kwargs):
        instance = kwargs.pop('instance', None)

        super(UpdateOrder, self).__init__(*args, **kwargs)

        if instance:
            self.fields['order_id'].initial = instance.order_id
            self.fields['customer_name'].initial = instance.customer_name
            self.fields['order_name'].initial = instance.order_name
            self.fields['order_quantity'].initial = instance.order_quantity

class FindOrder(forms.Form):
    order_id = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'class':'form-control' , 'placeholder': 'Order ID'}))

class LogIn(forms.Form):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class':'form-control' , 'placeholder': 'Email'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class':'form-control' , 'placeholder': 'Password'}))