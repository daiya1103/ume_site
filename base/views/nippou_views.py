from django.urls import reverse
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.views.generic import ListView, CreateView

from base.forms import ProfileForm
from base.models import User, Profile, Nippou

class NippouListView(ListView):
    model = Nippou
    template_name = 'base/nippou.html'

class NippouCreateView(CreateView):
    model = Nippou
    fields = (
        'date',
        'sales',
        'revenue',
        'plan',
    )
    template_name = 'base/nippou_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, '日報を提出しました')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('base:index')