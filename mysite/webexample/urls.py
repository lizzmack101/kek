# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.views.generic import ListView, DetailView
from webexample.models import Schedule

urlpatterns = [
    url(r'^$', ListView.as_view(queryset= Schedule.objects.all().order_by("id")[:15],
    template_name="schedule/post.html") ),
    url(r'^(?P<pk>\d+)$', DetailView.as_view(model = Schedule,
    template_name = "schedule/schedule.html")),
]
