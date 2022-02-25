from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView, FormView

from apps.poll.models import Poll
from apps.question.mixins import QuestionPermissionMixin
from .forms import QuestionCreateForm
from .models import Answer, Question


class QuestionCreateView(LoginRequiredMixin, FormView):
    """
    A view that creates a question, this view need a valid for create the question
    """

    form_class = QuestionCreateForm
    template_name = 'question/new.html'

    def dispatch(self, request, *args, **kwargs):
        # Check if the poll id was given, if not the user is redirect
        if not 'poll_id' in request.GET or request.GET.get('poll_id') == '':
            return redirect(reverse_lazy('poll:dashboard'))

        # Check if the poll exists, if not the user is redirect
        try:
            poll_id = self.request.GET.get('poll_id', '')
            poll_object = Poll.objects.get(id=poll_id)
            if poll_object.status == 'published':
                messages.add_message(
                    request, messages.INFO, 'You can not edit this poll anymore'
                )
                return redirect(reverse_lazy('poll:edit', kwargs={'pk': poll_id}))
        except Poll.DoesNotExist:
            messages.add_message(request, messages.INFO, 'Poll does not exist')
            return redirect(reverse_lazy('poll:dashboard'))

        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        # Get data from form
        question = form.cleaned_data['question']
        answers = [
            form.cleaned_data['answer1'],
            form.cleaned_data['answer2'],
            form.cleaned_data['answer3'],
        ]

        # Get poll object
        poll_id = self.request.GET.get('poll_id', '')
        poll_object = Poll.objects.get(id=poll_id)

        # Set url
        self.success_url = reverse_lazy('poll:edit', kwargs={'pk': poll_id})

        # Create question
        question = Question.objects.create(question=question, poll=poll_object)
        question.save()

        # Create answers
        for answer_text in answers:
            answer = Answer.objects.create(answer=answer_text, question=question)
            answer.save()

        return super().form_valid(form)


class QuestionEditView(QuestionPermissionMixin, LoginRequiredMixin, FormView):
    """
    A view that edits a question
    """

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
    """
    A view that deletes a question
    """

    model = Question

    def get_success_url(self):
        return reverse_lazy(
            'poll:edit', kwargs={'pk': self.request.session.get('poll_id')}
        )
