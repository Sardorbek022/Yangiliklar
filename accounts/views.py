from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

from .forms import (
    LoginForm
)


class UserLogin(View):
    def get(self, request):
        form = LoginForm()
        
        context = {
                'form' : form
            }
        
        return render(request=request, template_name='account/login.html', context=context)


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
                
                return render(request=request, template_name='account/login.html', context=context)
        else:
            
            context = {
                'form': form
            }
            
            return render(request=request, template_name='account/login.html', context=context)

       
        
class DashboardView(View):
    def get(self,request):
        user = request.user
        context = {
            'user' : user
        }
        
        return render(request=request, template_name='pages/user_profile.html', context=context)    