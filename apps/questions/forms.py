from django import forms


class QuestionCreateForm(forms.Form):
    question = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=255
    )
    answer1 = forms.CharField(
        label='Answer 1',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=100,
    )
    answer2 = forms.CharField(
        label='Answer 2',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=100,
    )
    answer3 = forms.CharField(
        label='Answer 3',
        widget=forms.TextInput(attrs={'class': 'form-control input-sm'}),
        max_length=100,
    )
