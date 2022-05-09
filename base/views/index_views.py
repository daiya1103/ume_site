from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django_pandas.io import read_frame
from base.models import User, Nippou

import pandas as pd
import datetime

# Create your views here.

class Index(ListView):
    template_name = 'base/index.html'
    model = User

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_nippou =  Nippou.objects.filter(user=self.request.user).values('revenue','date').order_by('date')
        df_nippou = read_frame(user_nippou)
        df_nippou['date'] = pd.to_datetime(df_nippou['date'])
        mm = df_nippou.set_index(['date'])
        all_sum_of_revenue = mm.resample(rule='M').sum()
        sum_of_revenue = all_sum_of_revenue['revenue'].tolist()[-1]
        context['sum_of_revenue'] = sum_of_revenue
        return context

def login(request):
    context = {}
    return render(request, 'pages/login.html', context)

import sys
sys.dont_write_bytecode = True