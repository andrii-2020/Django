from django import forms

from .models import Owner, Animals


#class OrderForm(forms.ModelForm):
  #  class Meta:
 #       model = OrderM
#        fields = ('animal', 'name', 'phone',)


class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ('name', 'first_name', 'age', 'date')


class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animals
        fields = ('owner_animals', 'name', 'age', 'description', 'type', 'photo',)