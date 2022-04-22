from django.urls import reverse
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.views.generic import ListView, CreateView, DetailView
from django.db.models import Q

from base.forms import ProfileForm
from base.models import User, Profile, Nippou, Output

class OutputListView(ListView):
    model = Output
    template_name = 'base/nippou.html'

    def get_queryset(self):
        query = self.request.GET.get('query')
        if query:
            object_list = Output.objects.filter(
                Q(question__icontains=query) | Q(description__icontains=query)
            )
        else:
            object_list = Output.objects.all()
        return object_list

class OutputCreateView(CreateView):
    model = Output
    fields = (
        'question',
        'description',
    )
    template_name = 'base/output_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        print(form)
        messages.success(self.request, 'アウトプットを作成しました')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('base:index')


class OutputDetailView(DetailView):
    model = Output
    template_name = 'base/output_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['output'] = Output.objects.get(pk=self.kwargs['pk'])
        return context