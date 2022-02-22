from django.http.response import Http404
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import FormView


# from django.views.generic.edit import FormView

from apps.poll.models import Poll
from apps.vote.forms import VoteForm


class VotePollView(FormView):
    template_name = 'vote/vote.html'
    form_class = VoteForm
    success_url = reverse_lazy('poll:dashboard')

    # Pass request for validate my user
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        poll_code = self.request.GET.get('code', '')

        # try:
        #     questions = Poll.objects.get(code=poll_code).question_set.all()
        # except Poll.DoesNotExist:
        #     questions = None

        if 'code' in self.request.GET:
            poll_object = get_object_or_404(Poll, code=poll_code)
            questions = poll_object.question_set.all()
        else:
            questions = None

        kwargs.update({'questions': questions})
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        poll_code = self.request.GET.get('code', '')

        if 'code' in self.request.GET:
            poll_object = get_object_or_404(Poll, code=poll_code)
            poll_titulo = poll_object.name
            context['poll_titulo'] = poll_titulo

        poll_titulo = None

        return context

    # def form_valid(self, form):
    #     print('pase')
    #     poll_code = self.request.GET.get('code', '')
    #     questions = Poll.objects.get(code=poll_code).question_set.all()
    #
    #     for question in questions:
    #         print(form.cleaned_data[question.question])
    #
    #     self.success_url = reverse_lazy('poll:dashboard')
    #     return super().form_valid(form)
