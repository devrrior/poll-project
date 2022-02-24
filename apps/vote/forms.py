from django import forms
from apps.poll.models import Poll


class VoteForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        questions = kwargs.pop('questions')  # store value of request
        super().__init__(*args, **kwargs)

        if questions != None:
            for question in questions:
                field_name = f'question_{question.id}'
                choices = []

                # self.fields[field_name] = forms.ModelChoiceField(widget=forms.RadioSelect(attrs={'class':'form-check-input'}), queryset=question.answer_set.all())
                for answer in question.answer_set.all():
                    choices.append((answer.id, answer.answer))

                self.fields[field_name] = forms.ChoiceField(
                    label=question.question,
                    required=True,
                    choices=choices,
                    widget=forms.RadioSelect,
                )
        
    def clean(self):
        poll_code = self.request.GET.get('code', '')
        questions = Poll.objects.get(code=poll_code).question_set.all()

        i = 1
        for question in questions:
            answer_id = self.cleaned_data.get(f'question_{i}')
            answer_object = question.answer_set.get(id=answer_id)
            answer_object.votes += 1
            answer_object.save()
            i += 1

        return super().clean()
