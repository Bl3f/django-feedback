#! /usr/bin/python
# -*- coding: utf-8 -*-

from django.forms import ModelForm, Select, Textarea, TextInput

from const import TYPE_CHOICES
from models import FeedbackMessage


class FeedbackForm(ModelForm):
    class Meta:
        model = FeedbackMessage
        fields = ('type', 'subject', 'content')
        widgets = {
            'type': Select(choices=TYPE_CHOICES, attrs={'class': 'form-control'}),
            'subject': TextInput(attrs={'class': 'form-control'}),
            'content': Textarea(attrs={'class': 'form-control'}),
        }
