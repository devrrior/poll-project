from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib import messages

from apps.question.models import Question


class QuestionPermissionMixin(object):
    """
    A mixin that checks if the question belong to the user
    """

    def dispatch(self, request, *args, **kwargs):
        id = self.kwargs.get('pk')
        question_object = get_object_or_404(Question, id=id)
        if self.request.user != question_object.poll.created_by:
            messages.add_message(
                request, messages.INFO, 'This question does not belong to you'
            )
            return redirect(reverse_lazy('poll:dashboard'))

        if question_object.poll.status == 'published':
            messages.add_message(
                request, messages.INFO, 'You can not edit this poll anymore'
            )
            return redirect(
                reverse_lazy('poll:edit', kwargs={'pk': question_object.poll.id})
            )
        return super().dispatch(request, *args, **kwargs)
