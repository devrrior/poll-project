from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages
from django.http.response import HttpResponseRedirect

from apps.poll.models import Poll


class PollPermissionMixin(object):
    def dispatch(self, request, *args, **kwargs):
        id = self.kwargs.get('pk')
        poll_object = get_object_or_404(Poll, id=id)
        if self.request.user != poll_object.created_by:
            messages.add_message(request, messages.INFO, 'This poll does not belong to you')
            return HttpResponseRedirect(reverse_lazy('poll:dashboard'))
        return super().dispatch(request, *args, **kwargs)
