from django.forms import ModelForm
from django import forms
from .models import Listing, CATEGORY_CHOICES

class ListingForm(ModelForm):
	title = forms.CharField(widget=forms.TextInput(
		attrs={
			'class': 'form-control'
		}
	))

	description = forms.CharField(required=False, widget=forms.Textarea(
		attrs={
			'class': 'form-control'
		}
	))

	starting_bid = forms.IntegerField(widget=forms.NumberInput(
		attrs={
			'class': 'form-control'
		}
	))

	picture = forms.URLField(required=False, widget=forms.URLInput(
		attrs={
			'class': 'form-control'
		}
	))
	
	category = forms.CharField(required=False, widget=forms.Select(
		choices=tuple([(None, 'None')] + list(CATEGORY_CHOICES.CATEGORY_CHOICES)),
		attrs={
			'class': 'form-control'
		}
	))

	class Meta:
		model = Listing
		fields = [ 
			'title',
			'description',
			'starting_bid',
			'picture',
			'category'
			]
		widget = {
			'title': 2
		}