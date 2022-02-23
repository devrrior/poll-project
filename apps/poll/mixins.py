from django.urls import reverse_lazy
from django.contrib import messages
from django.http.response import HttpResponseRedirect

from apps.poll.models import Poll


class PollPermissionMixin(object):
    def dispatch(self, request, *args, **kwargs):
        id = self.kwargs.get('pk')
        if self.request.user != Poll.objects.get(id=id).created_by:
            print('no te pertenece estooo!')
            print('user from self' + self.request.user)
            messages.add_message(request, messages.INFO, 'This poll does not belong to you')
            return HttpResponseRedirect(reverse_lazy('poll:dashboard'))
        return super().dispatch(request, *args, **kwargs)
