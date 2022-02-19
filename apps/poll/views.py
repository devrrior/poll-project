from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


from .forms import PollCreateForm
from .models import Poll


class PollCreateView(LoginRequiredMixin, CreateView):
    model = Poll
    form_class = PollCreateForm
    template_name = 'poll/dashboard.html'
    success_url = reverse_lazy('poll:dashboard')

    def get_context_data(self, **kwargs):
        kwargs['object_list'] = Poll.objects.all()
        return super().get_context_data(**kwargs)


class PollDetailView(DetailView):
    model = Poll
    template_name = 'poll/edit.html'

    def get(self, request, pk, *args, **kwargs):
        request.session['poll_id'] = pk
        return super().get(request, *args, **kwargs)


class PollDeleteView(DeleteView):
    model = Poll
    success_url = reverse_lazy('poll:dashboard')

