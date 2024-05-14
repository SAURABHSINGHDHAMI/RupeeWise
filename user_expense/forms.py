from django import forms
from .models import Bill, Cloth, Food, Travel, Subscription, Miscellaneous

class BillForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = ['name', 'amount']

class ClothForm(forms.ModelForm):
    class Meta:
        model = Cloth
        fields = ['name', 'amount']

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['name', 'amount']

class TravelForm(forms.ModelForm):
    class Meta:
        model = Travel
        fields = ['name', 'amount']

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['name', 'amount']

class MiscellaneousForm(forms.ModelForm):
    class Meta:
        model = Miscellaneous
        fields = ['name', 'amount']