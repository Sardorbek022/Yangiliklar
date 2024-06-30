from django.shortcuts import render
from django.views import View

from .models import (
    NewsModel, ContactModel, CategoryModel
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
    
    
class NewsDetailPage(View):
    
    def get(self, request):
        return render(request=request, template_name='news/news_detail.html')
    
    
class CategoryDetailPage(View):
    
    def get(self, request):
        return render(request=request, template_name='news/category_detail.html')
