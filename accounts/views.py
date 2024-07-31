from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import (
    LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
)
from .models import (
    ProfileModel
)


class UserLogin(View):
    def get(self, request):
        form = LoginForm()
        print(form)
        
        context = {
                'form' : form
            }
        
        return render(request=request, template_name='registration/login.html', context=context)


    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home_page')
                else:
                    return HttpResponse('Sizning profilingiz faol holatda emas')
            else:
                
                context = {
                    'form': form,
                }
                
                return render(request=request, template_name='registration/login.html', context=context)
        else:
            
            context = {
                'form': form
            }
            
            return render(request=request, template_name='registration/login.html', context=context)

            
class DashboardView(LoginRequiredMixin, View):
    def get(self,request):
        user = request.user
        profile = ProfileModel.objects.get(user=user)
        context = {
            'user' : user,
            'profile' : profile
        }
        
        return render(request=request, template_name='pages/user_profile.html', context=context)    
    
    
def UserRegistrationView(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data["password"])
            new_user.save()
            ProfileModel.objects.create(user=new_user)
            context = {"new_user": new_user}
            return render(request, 'account/register_done.html', context)
        else:
            context = {"user_form": user_form, "error": "Forma noto‘g‘ri to‘ldirilgan"}
            return render(request, 'account/register.html', context)
    else:
        user_form = UserRegistrationForm()
        context = {"user_form": user_form}
        return render(request, 'account/register.html', context)
    

# class SignUpView(CreateView):
    
#     form_class = UserCreationForm
#     success_url = reverse_lazy('home_page')
#     template_name = 'account/register.html'


@login_required
def Edit_User_View(request):
    
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST,)
        profile_form = ProfileEditForm(instance=request.user.profile,
                                       data=request.POST,
                                       files=request.FILES)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            
            return redirect('user_profile_page')
            
    else:
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile)
    
    return render(request=request, template_name='pages/user_edit.html', context={'user_form' : user_form, 'profile_form' : profile_form})


class EditUserView(LoginRequiredMixin, View):
    
    def get(self, request):
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile)
    
        return render(request=request, template_name='pages/user_edit.html', context={'user_form' : user_form, 'profile_form' : profile_form})

    
    def post(self, request):
        user_form = UserEditForm(instance=request.user, data=request.POST,)
        profile_form = ProfileEditForm(instance=request.user.profile,
                                                    data=request.POST,
                                                    files=request.FILES)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            
            return redirect('user_profile_page')