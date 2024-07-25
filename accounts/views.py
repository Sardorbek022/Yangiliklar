from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

from .forms import (
    LoginForm, UserRegistrationForm
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
                print(form)
                
                return render(request=request, template_name='registration/login.html', context=context)
        else:
            
            context = {
                'form': form
            }
            
            return render(request=request, template_name='registration/login.html', context=context)

       
        
class DashboardView(View):
    def get(self,request):
        user = request.user
        context = {
            'user' : user
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
