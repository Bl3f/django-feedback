#! /usr/bin/python
# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.db import models


class FeedbackMessage(models.Model):
    type = models.CharField(max_length=10, null=False, blank=False, db_index=True)
    subject = models.CharField(max_length=50, null=True, blank=True)
    content = models.CharField(max_length=1023, null=False, blank=False)
    user = models.ForeignKey(User, db_index=True)