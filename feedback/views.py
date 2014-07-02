#! /usr/bin/python
# -*- coding: utf-8 -*-

from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView

from forms import FeedbackForm
from models import FeedbackMessage


class FeedbackView(TemplateView):
    template_name = "feedback/index.html"

    def get(self, request, *args, **kwargs):
        return super(FeedbackView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = FeedbackForm(data=request.POST)

        if form.is_valid():
            data = form.cleaned_data

            feedback_message = FeedbackMessage()
            feedback_message.type = data.get('type')
            feedback_message.subject = data.get('subject')
            feedback_message.content = data.get('content')
            feedback_message.user = request.user
            feedback_message.save()

            message = (u"[FEEDBACK ADHOC] {0}: {1}".format(feedback_message.type.capitalize(), feedback_message.subject),
                       u"{0}\n- - - - - - - - - -\nFrom user: {1}".format(feedback_message.content,
                                                                          feedback_message.user.username,
                                                                          ),
                       feedback_message.user.email,
                       getattr(settings, 'EMAIL_FOR', None),
                       )

            send_mail(*message, fail_silently=False)

            return HttpResponse('true')
        else:
            context = super(FeedbackView, self).get_context_data(**kwargs)
            context.update({
                'form': form,
            })
            return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super(FeedbackView, self).get_context_data(**kwargs)
        context.update({
            'form': FeedbackForm(),
        })

        return context


class FeedbackList(ListView):
    model = FeedbackMessage
    template_name = 'feedback/list.html'
    groups = ['Createur']

    def get_queryset(self):
        return FeedbackMessage.objects.all()