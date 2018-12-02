"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.views.generic import ListView, DetailView
from News.models import Student

urlpatterns = [
    url(r'^$', ListView.as_view(queryset=Student.objects.all().order_by("id")[:15],
    template_name="news/post.html") ),
    url(r'^(?P<pk>\d+)$', DetailView.as_view(model = Student,
    template_name = "news/student.html")),
]
