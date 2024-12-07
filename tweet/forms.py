from django import forms
from . models import Tweet

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text', 'photo']    #yesma models.py ma jj field xa tei tei array ma rakhney 