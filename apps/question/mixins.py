from django.urls import reverse_lazy
from django.contrib import messages
from django.http.response import HttpResponseRedirect

from apps.question.models import Question



class QuestionPermissionMixin(object):
    def dispatch(self, request, *args, **kwargs):
        id = self.kwargs.get('pk')
        if self.request.user != Question.objects.get(id=id).poll.created_by:
            print('no te pertenece estooo!')
            messages.add_message(request, messages.INFO, 'This question does not belong to you')
            return HttpResponseRedirect(reverse_lazy('poll:dashboard'))
        return super().dispatch(request, *args, **kwargs)
