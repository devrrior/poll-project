from django.urls import reverse_lazy
from django.views.generic.edit import FormView

from apps.poll.models import Poll
from .forms import QuestionCreateForm
from .models import Answer, Question


class QuestionCreateView(FormView):
    form_class = QuestionCreateForm
    template_name = 'question/new.html'

    def form_valid(self, form):
        # Get dato from form
        question = form.cleaned_data['question']
        answers = [
            form.cleaned_data['answer1'],
            form.cleaned_data['answer2'],
            form.cleaned_data['answer3'],
        ]

        # Get poll object
        poll_id = self.request.session.get('poll_id')
        poll = Poll.objects.get(id=poll_id)

        # Set url
        self.success_url = reverse_lazy(
            'poll:edit', kwargs={'pk': self.request.session.get('poll_id')}
        )

        # Delete session
        del self.request.session['poll_id']

        # Create question
        question = Question.objects.create(question=question, poll=poll)
        question.save()

        # Create answers
        for answer_text in answers:
            answer = Answer.objects.create(answer=answer_text, question=question)
            answer.save()

        return super().form_valid(form)

class QuestionEditView(FormView):
    form_class = QuestionCreateForm
    template_name = 'question/edit.html'

    def get_initial(self, *args, **kwargs):
        initial = super().get_initial(**kwargs)
        initial['question']
        initial['answer1']
        initial['answer2']
        initial['answer3']
        return super().get_initial()

