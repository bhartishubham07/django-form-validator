from django import forms
from django.http import HttpResponse
from django.core import validators
    
    
class StudentForm(forms.Form):
    Username = forms.CharField(max_length=15, validators=[validators.MaxLengthValidator(10)])
    password = forms.CharField(max_length=15, widget=forms.PasswordInput)
    Confirm_password = forms.CharField(max_length=15, widget=forms.PasswordInput)
    botcatcher = forms.CharField(max_length=100, widget=forms.HiddenInput, required=False)
    
    
    def clean(self):
        pas = self.cleaned_data['password']
        cpas = self.cleaned_data['Confirm_password']
        if pas != cpas:
            raise forms.ValidationError('Password mismatched')
        
        
    def clean_botcatcher(self):
        bot = self.cleaned_data['botcatcher']
        if len(bot)>0:
            raise forms.ValidationError('Bot is trying to insert data')