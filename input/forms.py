from django import forms


class InputForm(forms.Form):
    srch = forms.CharField(label='Search', max_length=10000)
    dateFrom = forms.DateField(label='DateFrom')
    dateTo = forms.DateField(label='dateTo')
    states1 = forms.ChoiceField(label='Category')
    states2 = forms.ChoiceField(label='Acts')
    states3 = forms.ChoiceField(label='Judge')
