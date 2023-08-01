from django import forms
from django.core import validators

class contactForm(forms.Form):
    name=forms.CharField(label="Full Name:", help_text="Enter your full name",
    required=False, widget=forms.Textarea (attrs={'id' : 'text_area', 'placeholder' : 'Enter your name'}))
   
   
    email=forms.EmailField(label="User Email", required=False)
    # weight=forms.FloatField()
    # balance=forms.DecimalField()
    # age=forms.CharField(widget=forms.NumberInput, required=False)
    # check=forms.BooleanField()
    # bithday=forms.CharField(widget=forms.DateInput(attrs={'type' : 'date'}))
    # appointment=forms.CharField(widget=forms.DateInput(attrs={'type' : 'datetime-local'}))
    # CHOICES=[('small', 'small'), ('Medium', 'medium'),('Large','Large')]
    # choice=forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    # MEAL=[('p','peparoni'),('M','Mashroom'),('B', 'Beef')]
    # pizza=forms.MultipleChoiceField(choices=MEAL, widget=forms.CheckboxSelectMultiple)
    
# class StudentData(forms.Form):
#     name=forms.CharField(widget=forms.TextInput)
#     email=forms.CharField(widget=forms.TextInput)
    
#     def clean(self):
#         cleaned_dat=super().clean()
#         valname=self.cleaned_data['name']
#         valemail=self.cleaned_data['email']
        
#         if len(valname)<10:
#             raise forms.ValidationError('Enter a name atleast 10 characters')
#         if ".com" not in valemail:
#             raise forms.ValidationError("Your email must contain .com")


def len_check(value):
    if len(value)<10:
        raise forms.ValidationError("Enter value at least 10 character")

class StudentData(forms.Form):
    name=forms.CharField(validators=[validators.MaxLengthValidator
    (10, message='ENter a name at leat 10 character')])
    text=forms.CharField(widget=forms.TextInput, validators=[len_check])
    email=forms.CharField(widget=forms.EmailInput, validators=[validators.EmailValidator(message= "Enter a valid Email")])
    age =forms.IntegerField(validators=[validators.MaxValueValidator(25, message="value less than 25"),
        validators.MinValueValidator(14, message="value should more than 14")])
    file=forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf'], message="only pdf is excepted")])