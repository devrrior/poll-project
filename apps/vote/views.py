from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView


# from django.views.generic.edit import FormView

from apps.poll.models import Poll
from apps.vote.forms import VoteForm


class VotePollView(FormView):
    template_name = 'vote/vote.html'
    form_class = VoteForm
    success_url = reverse_lazy('thanks')

    # Pass request for validate my user
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()

        if 'code' in self.request.GET:
            poll_code = self.request.GET.get('code', '')
            poll_object = get_object_or_404(Poll, code=poll_code)
            questions = poll_object.question_set.all()
        else:
            questions = None

        kwargs.update({'questions': questions, 'request': self.request })
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

class ThanksTemplateView(TemplateView):
    template_name = 'vote/thanks.html'
