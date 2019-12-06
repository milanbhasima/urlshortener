from django import forms
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from .validators import validate_url, validate_dot_com

class SubmitForm(forms.Form):
	url=forms.CharField(label='Submit url', validators=[validate_url], widget=forms.TextInput(attrs={"placeholder":"Long URl...","class":"form-control"}))

	# def clean(self):
	# 	cleaned_data=super(SubmitForm,self).clean()
	# 	url=cleaned_data.get('url')
	# 	url_validator=URLValidator()
	# 	try:
	# 		url_validator(url)
	# 	except:
	# 		raise forms.ValidationError("Invalid URL for this field")
	# 	return url

	# def clean_url(self):
	# 	url=self.cleaned_data['url']
	# 	url_validator=URLValidator()
	# 	try:
	# 		url_validator(url)
	# 	except:
	# 		raise forms.ValidationError("Invalid URL for this field")
	# 	return url