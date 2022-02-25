from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.base import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from apps.poll.mixins import PollPermissionMixin


from .forms import PollCreateForm
from .models import Poll


class PollCreateView(LoginRequiredMixin, CreateView):
    """
    A view that shows all polls which belong to the user, also in this view the user can create a Poll
    """

    model = Poll
    form_class = PollCreateForm
    template_name = 'poll/dashboard.html'
    success_url = reverse_lazy('poll:dashboard')

    def get_context_data(self, **kwargs):
        kwargs['object_list'] = Poll.objects.filter(created_by=self.request.user)
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        # Set author to poll
        poll_object = form.save(commit=False)
        poll_object.created_by = self.request.user
        poll_object.save()
        return super().form_valid(form)


class PollDetailView(PollPermissionMixin, LoginRequiredMixin, DetailView):
    """
    A view that shows attributes of a Poll, here the user can do the following:
    - Create Question
    - Publish Poll
    - Edit Question

    Also if the poll is published, the user can see a graphic per question
    """

    model = Poll
    template_name = 'poll/edit.html'


class PollDeleteView(PollPermissionMixin, LoginRequiredMixin, DeleteView):
    """
    A view that deletes a Poll
    """

    model = Poll
    success_url = reverse_lazy('poll:dashboard')


class PollPublishView(PollPermissionMixin, LoginRequiredMixin, View):
    """
    A view that publis a Poll
    """

    def get(self, request, *args, **kwargs):
        id = self.kwargs.get('pk')
        next = request.GET.get('next', '/')
        poll_object = Poll.objects.get(id=id)
        poll_object.status = 'published'
        poll_object.save()
        return HttpResponseRedirect(next)
