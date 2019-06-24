from django import forms
from . models import Image,Profile,Comments,Followers

class PostImage(forms.ModelForm):
    class Meta:
        model=Image
        exclude=['likes','comments','date','user','userId','profile']