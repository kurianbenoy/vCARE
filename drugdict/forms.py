from django import forms
from .models import UploadDrug

class DrugForm(forms.ModelForm):

	class Meta:
		model=UploadDrug
		fields=['pillname','sideeffects','warning','dosage']

