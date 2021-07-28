from django import forms
from . models import ContactModel

class ContactForm(forms.ModelForm):
    class Meta:
        model= ContactModel
        fields= '__all__'
        labels= {'name':'Name','email':'Email','message':'Message'}

        widgets={
        'name':forms.TextInput(attrs={'class':'form-control'}),
        'message':forms.Textarea(attrs={'class':'form-control'}),       
        'email':forms.EmailInput(attrs={'class':'form-control'})}