from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView, FormView

from apps.poll.models import Poll
from apps.question.mixins import QuestionPermissionMixin
from .forms import QuestionCreateForm
from .models import Answer, Question

# TODO change the way to add poll's id, send id by queryparams
class QuestionCreateView(LoginRequiredMixin, FormView):
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


class QuestionEditView(QuestionPermissionMixin, LoginRequiredMixin, FormView):
    form_class = QuestionCreateForm
    template_name = 'question/new.html'

    def get_initial(self, *args, **kwargs):
        initial = super().get_initial(**kwargs)
        id = self.kwargs.get('pk')
        question_object = Question.objects.get(id=id)
        initial['question'] = question_object.question
        i = 0
        for answer_object in question_object.answer_set.all():
            i += 1
            initial[f'answer{i}'] = answer_object.answer
            initial[f'answer{i}'] = answer_object.answer
            initial[f'answer{i}'] = answer_object.answer
        return initial

    def form_valid(self, form):
        id = self.kwargs.get('pk')
        question = form.cleaned_data['question']
        answers = {
            'answer1': form.cleaned_data['answer1'],
            'answer2': form.cleaned_data['answer2'],
            'answer3': form.cleaned_data['answer3'],
        }

        i = 0
        question_object = Question.objects.get(id=id)
        question_object.question = question
        question_object.save()
        for answer_object in question_object.answer_set.all():
            i += 1
            answer_object.answer = answers[f'answer{i}']
            answer_object.save()

        self.success_url = reverse_lazy(
            'poll:edit', kwargs={'pk': self.request.session.get('poll_id')}
        )

        return super().form_valid(form)


class QuestionDeleteView(QuestionPermissionMixin, LoginRequiredMixin, DeleteView):
    model = Question

    def get_success_url(self):
        return reverse_lazy(
            'poll:edit', kwargs={'pk': self.request.session.get('poll_id')}
        )
