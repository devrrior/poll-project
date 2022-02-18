from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView
from apps.polls.forms import PollCreateForm

from apps.polls.models import Poll


class PollCreateView(CreateView):
    model = Poll
    form_class = PollCreateForm
    template_name = 'polls/dashboard.html'
    success_url = reverse_lazy('polls:dashboard')

    def get_context_data(self, **kwargs):
        kwargs['object_list'] = Poll.objects.all()
        return super().get_context_data(**kwargs)


class PollEditView:
    pass


class PollDeleteView(DeleteView):
    model = Poll
    success_url = reverse_lazy('polls:dashboard')
