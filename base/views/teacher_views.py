from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.views.generic import ListView, DetailView, UpdateView
from django.utils import timezone
from django.http import JsonResponse
from django.conf import settings
