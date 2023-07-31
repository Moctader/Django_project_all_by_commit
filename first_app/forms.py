from django import forms

class contactForm(forms.Form):
    name=forms.CharField(label="User Name")
    file=forms.FileField()
    
    
    
    
    
    
    
    # email=forms.EmailField(label="User Email")
    # age=forms.IntegerField()
    # weight=forms.FloatField()
    # balance=forms.DecimalField()
    # check=forms.BooleanField()
    # bithday=forms.DateField()
    # appointment=forms.DateTimeField()
    # CHOICES=[('s', 'small'), ('M', 'medium'),('L','Large')]
    # choice=forms.ChoiceField(choices=CHOICES)
    # MEAL=[('p','peparoni'),('M','Mashroom'),('B', 'Beef')]
    # pizza=forms.MultipleChoiceField(choices=MEAL)