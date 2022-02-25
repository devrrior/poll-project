from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib import messages

from apps.poll.models import Poll


class PollPermissionMixin(object):
    """
    A mixin that checks if the poll belong to the user
    """

    def dispatch(self, request, *args, **kwargs):
        id = self.kwargs.get('pk')
        poll_object = get_object_or_404(Poll, id=id)
        if self.request.user != poll_object.created_by:
            messages.add_message(
                request, messages.INFO, 'This poll does not belong to you'
            )
            return redirect(reverse_lazy('poll:dashboard'))
        return super().dispatch(request, *args, **kwargs)
