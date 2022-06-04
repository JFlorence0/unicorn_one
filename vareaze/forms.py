from django import forms
from .models import Contract

class ContractForm(forms.ModelForm):
	expiration_date = forms.DateField(widget= forms.SelectDateWidget)
	class Meta:
		model = Contract
		fields = ['expiration_date', 'vareaze_id', 'sent_to']
		labels = {
			'expiration_date': 'Expiration Date',
			'vareaze_id': 'Vareaze ID',
			'sent_to': 'Other Party',
		}