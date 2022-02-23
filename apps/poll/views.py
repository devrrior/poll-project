from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.base import View
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
        kwargs['object_list'] = Poll.objects.filter(created_by=self.request.user)
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class PollDetailView(LoginRequiredMixin,DetailView):
    model = Poll
    template_name = 'poll/edit.html'

    def get(self, request, *args, **kwargs):
        id = self.kwargs.get('pk')
        request.session['poll_id'] = id
        return super().get(request, *args, **kwargs)


class PollDeleteView(LoginRequiredMixin, DeleteView):
    model = Poll
    success_url = reverse_lazy('poll:dashboard')

class PollPublishView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        id = self.kwargs.get('pk')
        next = request.GET.get('next', '/')
        poll_object = Poll.objects.get(id=id)
        poll_object.status = 'published'
        poll_object.save()
        return HttpResponseRedirect(next)
