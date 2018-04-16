from django import forms
from . import models

class UserForm(forms.ModelForm):
    userid = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    about = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = models.User
        fields = ('userid', 'password', 'name',  'about')

class RatingForm(forms.ModelForm):
    # if user1.canRate = 1 and edit if canEdit = 1
    rating = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = models.Rating
        # fields = ('user1', 'user2', 'rating')
        fields = ('rating', )

class WorkForm(forms.ModelForm):
    class Meta:
        model = models.Work
        fields = ('user', 'work')

class LoginForm(forms.Form):
    userid = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    # class Meta:
    #     model = models.User
    #     fields = ('userid', 'password')

class SudoForm(forms.Form):
    CHOICES=[( True ,'Enable'), # Make strings if True and False naievly doesn't work
            (False,'Disable')]
    
    EveryoneCanSee  = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), label="Everyone Can See")
    EveryoneCanRate = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), label="Everyone Can Rate")
    EveryoneCanEdit = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), label="Everyone Can Edit")
    
   