from django.urls import reverse_lazy
from django.http.response import HttpResponseRedirect

from apps.question.models import Question



class QuestionPermissionMixin(object):
    def dispatch(self, request, *args, **kwargs):
        id = self.kwargs.get('pk')
        if self.request.user != Question.objects.get(id=id):
            print('no te pertenece estooo!')
            return HttpResponseRedirect(reverse_lazy('poll:dashboard'))
        return super().dispatch(request, *args, **kwargs)
