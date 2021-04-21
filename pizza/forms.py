from django import forms
from .models import Pizza,Size

# class PizzaForms(forms.Form):
#     topping1 = forms.CharField(max_length=100, label='Topping 1')
#     topping2 = forms.CharField(max_length=100, label='Topping 2')
#     size = forms.ChoiceField(choices=[('Small', 'Small'),('Medium', 'Medium'),('Large','Large')], label= 'Size')

class PizzaForms(forms.ModelForm):


    class Meta:
        model = Pizza
        fields = ['topping1', 'topping2', 'size']
        labels = {'topping1': 'Topping 1', 'topping2': 'Topping 2'}

class MultiplePizzaForms(forms.Form):
    number = forms.IntegerField(min_value=2, max_value=10)