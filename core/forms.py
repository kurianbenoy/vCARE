from django import forms
from .models import Messages

class MessageForm(forms.ModelForm):

	class Meta:
		model=Messages
		fields=['name','email','comments']

