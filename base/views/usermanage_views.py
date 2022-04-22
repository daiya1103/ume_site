import cv2
import base64
import numpy as np
import os

from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.views.generic import ListView, DetailView, UpdateView
from django.utils import timezone
from django.http import JsonResponse
from django.conf import settings

from base.forms import ProfileForm
from base.models import User, Profile

class MyLoginView(LoginView):
    template_name = 'base/login.html'

    def form_valid(self, form):
        messages.success(self.request, 'ログイン完了！')
        return super().form_valid(form)

def profileform(request):
    profile = request.user.profile
    icon = profile.icon
    dream = profile.dream
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            if not profile.icon:
                profile.icon = icon
            elif not profile.dream:
                profile.dream = dream
            profile.save()
            messages.success(request, 'プロフィールが変更されました')
    else:
        form = ProfileForm(request.POST, request.FILES)
    return render(request, 'base/profile_form.html', {'form': form})

class ProfileListView(ListView):
    model = Profile
    template_name = 'base/profile_list.html'

class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'base/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.get(pk=self.kwargs['pk'])
        return context

def profileImageUpload(request):
    ''' プロフィール編集画面からPOSTされた画像データの保存処理 '''
    # POSTされたb64データを元の画像データにデコード
    image_data = base64.b64decode(request.POST.get('image').split(',')[1])
    image_binary = np.frombuffer(image_data, dtype=np.uint8)
    image = cv2.imdecode(image_binary, cv2.IMREAD_COLOR)
    temp_name = 'templateImage.png'
    cv2.imwrite(temp_name, image)

    # 画像データをリネームして移動
    dt_now = timezone.now()
    file_name = '/profileImage/' + str(request.user.pk).zfill(8) + '_' + dt_now.strftime("%Y%m%d%H%M%S") + '.png'
    os.rename(temp_name, settings.MEDIA_ROOT + file_name)

    # 保存した画像を登録
    profile = get_object_or_404(Profile, pk=request.user.profile.pk)
    profile.profileImage = file_name
    profile.save()

    data = {'imageURL' : profile.profileImage.url}
    return JsonResponse(data)