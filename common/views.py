from django.shortcuts import render  
from django.contrib.auth.forms import AuthenticationForm  
from django.contrib import auth  
from django.http.response import HttpResponseRedirect  
from django.urls import reverse_lazy  

from django.views.generic import FormView  
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth import login, authenticate  
from common.forms import ProfileCreationForm, ProfileSocAccCreationForm  
from django.views.generic import  UpdateView

from common.models import UserProfile, SocialAccauntProfile

from allauth.socialaccount.models import SocialAccount
import uuid

# def profile(request):  
#     context = {}  
#     if request.user.is_authenticated:  
#         context['username'] = request.user.username
#         try:
#             # context['age'] = UserProfile.objects.get(user=request.user).age
#             context['github_url'] = SocialAccount.objects.get(provider='github', user=request.user).extra_data['html_url']
#         except SocialAccount.DoesNotExist:
            
#             try:
#                 context['age'] = UserProfile.objects.get(user=request.user).age
#             except UserProfile.DoesNotExist:
#                 pass
        
#     return render(request, 'profile.html', context)
   


def profile(request):  
    context = {}  
    if request.user.is_authenticated:  
        context['username'] = request.user.username
        try:
            soc_user = SocialAccount.objects.get(provider='github', user=request.user)
            try:
                context['name'] = SocialAccauntProfile.objects.get(user=soc_user).name
                context['age'] = SocialAccauntProfile.objects.get(user=soc_user).age
                context['city'] = SocialAccauntProfile.objects.get(user=soc_user).city
                context['github_url'] = SocialAccount.objects.get(provider='github', user=request.user).extra_data['html_url']
                context['id'] = SocialAccauntProfile.objects.get(user=soc_user).id             
                return render(request, 'profile.html', context)
                
            except SocialAccauntProfile.DoesNotExist:
                return HttpResponseRedirect(reverse_lazy('common:socprofile-create'))

        except SocialAccount.DoesNotExist:
            try:
                context['name'] = UserProfile.objects.get(user=request.user).name
                context['age'] = UserProfile.objects.get(user=request.user).age
                context['city'] = UserProfile.objects.get(user=request.user).city
                context['id'] = UserProfile.objects.get(user=request.user).id
            except UserProfile.DoesNotExist:
                return HttpResponseRedirect(reverse_lazy('common:profile-create'))
            # finally:
            #     return render(request, 'profile.html', context)
    return render(request, 'profile.html', context)




    

    
# def login(request):  
#     if request.method == 'POST':  
#         form = AuthenticationForm(request=request, data=request.POST)  
#         if form.is_valid():  
#             auth.login(request, form.get_user())  
#             return HttpResponseRedirect(reverse_lazy('common:index'))  
#     else:  
#         context = {'form': AuthenticationForm()}  
#         return render(request, 'login.html', context)  
  
  
# def logout(request):  
#     auth.logout(request)  
#     return HttpResponseRedirect(reverse_lazy('common:index'))

class RegisterView(FormView):  
  
    form_class = UserCreationForm  
  
    def form_valid(self, form):  
        form.save()  
        username = form.cleaned_data.get('username')  
        raw_password = form.cleaned_data.get('password1')  
        login(self.request, authenticate(username=username, password=raw_password))  
        return super(RegisterView, self).form_valid(form)  
  
  
class CreateUserProfile(FormView):

    success_url = reverse_lazy("common:profile")
    form_class = ProfileCreationForm  
    template_name = 'profile-create.html'  
	
    def dispatch(self, request, *args, **kwargs):  
        if self.request.user.is_anonymous:  
            return HttpResponseRedirect(reverse_lazy('common:login'))  
        return super(CreateUserProfile, self).dispatch(request, *args, **kwargs)  
  
    def form_valid(self, form):  
        instance = form.save(commit=False)  
        instance.user = self.request.user  
        instance.save()  
        return super(CreateUserProfile, self).form_valid(form)


class CreateSocUserProfile(FormView):

    success_url = reverse_lazy("common:profile")
    form_class = ProfileSocAccCreationForm  
    template_name = 'profile-create.html'  
	
    # def dispatch(self, request, *args, **kwargs):  
    #     if self.request.user.is_anonymous:  
    #         return HttpResponseRedirect(reverse_lazy('common:login'))  
    #     return super(CreateUserProfile, self).dispatch(request, *args, **kwargs)  
  
    def form_valid(self, form):  
        instance = form.save(commit=False) 
        soc_user = SocialAccount.objects.get(user=self.request.user)
        extra_data = soc_user.extra_data
        instance.user = soc_user
        instance.extra_data_profile = extra_data
        instance.save() 
        return super(CreateSocUserProfile, self).form_valid(form)


class ProfileUpdate(UpdateView):
    model = UserProfile
    form_class = ProfileCreationForm 
    success_url = reverse_lazy('common:profile')  
    template_name = 'profile-update.html'

class SocProfileUpdate(UpdateView):
    model = SocialAccauntProfile
    form_class = ProfileSocAccCreationForm
    success_url = reverse_lazy('common:profile')  
    template_name = 'profile-update.html'