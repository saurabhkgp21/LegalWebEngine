from django import forms


class InputForm(forms.Form):
	naturalLanguageQuery = forms.CharField(label='Search', max_length=10000)
	dateFrom = forms.DateField(label='DateFrom', required=False)
	dateTo = forms.DateField(label='dateTo', required=False)

	CATEGORIES = (
		('a', 'A'),
		('b', 'B')
	)

	ACTS = (
		('c', 'C'),
		('d', 'D')
	)

	JUDGES = (
		('e', 'E'),
		('f', 'F')
	)

	categories = forms.MultipleChoiceField(choices=CATEGORIES, widget=forms.CheckboxSelectMultiple(), label='Categories', required=False)
	acts = forms.MultipleChoiceField(choices=ACTS, widget=forms.CheckboxSelectMultiple(), label='Acts', required=False)
	judges = forms.MultipleChoiceField(choices=JUDGES, widget=forms.CheckboxSelectMultiple(), label='Judges', required=False)
