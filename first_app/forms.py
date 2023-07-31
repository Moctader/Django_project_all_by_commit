from django import forms

class contactForm(forms.Form):
    name=forms.CharField(label="Full Name:", help_text="Enter your full name",
    required=False, widget=forms.Textarea (attrs={'id' : 'text_area', 'placeholder' : 'Enter your name'}))
   
   
    email=forms.EmailField(label="User Email", required=False)
    # weight=forms.FloatField()
    # balance=forms.DecimalField()
    age=forms.CharField(widget=forms.NumberInput, required=False)
    check=forms.BooleanField()
    bithday=forms.CharField(widget=forms.DateInput(attrs={'type' : 'date'}))
    appointment=forms.CharField(widget=forms.DateInput(attrs={'type' : 'datetime-local'}))
    CHOICES=[('small', 'small'), ('Medium', 'medium'),('Large','Large')]
    choice=forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    MEAL=[('p','peparoni'),('M','Mashroom'),('B', 'Beef')]
    pizza=forms.MultipleChoiceField(choices=MEAL, widget=forms.CheckboxSelectMultiple)