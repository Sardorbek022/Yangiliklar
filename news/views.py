from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from .models import (
    NewsModel, ContactModel, CategoryModel
)

from .forms import (
    ContactForm, 
)


class HomePageView(View):
    
    def get(self,request):
        all_news_list = NewsModel.manager.all().order_by('-publish_time')
        uzb_news_list = NewsModel.manager.all().filter(category__name="O'ZBEKISTON").order_by('-publish_time')[:6]
        world_news_list = NewsModel.manager.all().filter(category__name="JAHON").order_by('-publish_time')[:6]
        science_technology_news_list = NewsModel.manager.all().filter(category__name="FAN-TEXNIKA").order_by('-publish_time')[:6]
        sport_news_list = NewsModel.manager.all().filter(category__name="SPORT").order_by('-publish_time')[:6]

        
        context = {
            'all_news_list' : all_news_list,
            'uzb_news_list' : uzb_news_list,
            'world_news_list' : world_news_list,
            'science_technology_news_list' : science_technology_news_list,
            'sport_news_list' : sport_news_list
        }

        return render(request=request, template_name='news/home.html', context=context)
    
    
class ContactPageView(View):
    
    def get(self, request):
            return render(request=request, template_name='news/contact.html')
    
    
    def post(self, request):
        
        form = ContactForm(request.POST)
    
        if form.is_valid():
            form.save()
            return redirect('home_page')
            
        return render(request=request, template_name='news/contact.html', context={'form':form})
        
    
    
class NewsDetailPage(View):
    
    def get(self, request, pk):
        
        # news_detail = NewsModel.objects.get(pk=pk)
        news_detail = get_object_or_404(NewsModel, pk=pk)
        
        
        context = {
            'news_detail' : news_detail
        }
        
        return render(request=request, template_name='news/news_detail.html', context=context)
    
    
class CategoryDetailPage(View):
    
    def get(self, request, pk):
        
        # category_detail = NewsModel.objects.get(pk=pk)
        category_detail = get_object_or_404(NewsModel, pk=pk)
        
        
        context = {
            'category_detail' : category_detail
        }
        
        return render(request=request, template_name='news/category_detail.html', context=context)
