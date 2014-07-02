#! /usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
                       url(r'^$', views.FeedbackView.as_view(), name='feedback'),
                       url(r'^list/$', views.FeedbackList.as_view(), name='feedback_list'),
                       )