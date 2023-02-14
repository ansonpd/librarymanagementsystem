from django import forms
from django.contrib.auth.models import User
from . import models

class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))

class AdminSigupForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']

class StudentUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
  
class StudentExtraForm(forms.ModelForm):
    class Meta:
        model=models.StudentExtra
        fields=['enrollment','branch']

class BookForm(forms.ModelForm):
    class Meta:
        model=models.Book
        fields=['name','isbn','author','category']

class IssuedBookForm(forms.Form):
    isbn2=forms.ModelChoiceField(queryset=models.Book.objects.all(),empty_label="Name and isbn", to_field_name="isbn",label='Name and Isbn')
    enrollment2=forms.ModelChoiceField(queryset=models.StudentExtra.objects.all(),empty_label="Name and enrollment",to_field_name='enrollment',label='Name and enrollment')
    

class ProductForm(forms.ModelForm):
    class Meta:
        model=models.Product
        fields=[ 'category', 'name', 'slug', 'image', 'description', 'price', 'stock']

class OrderCreateForm(forms.ModelForm):
 
	class Meta:
		model=models.Order
		fields = ['name', 'email', 'phone', 'address',  'district',  'payment_method',  'transaction_id']
