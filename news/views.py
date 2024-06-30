from django.shortcuts import render
from django.views import View

from .models import (
    NewsModel, ContactModel, CategoryModel
)


class HomePageView(View):
    
    def get(self,request):
        all_news_list = NewsModel.manager.all().order_by('-publish_time')
        
        context = {
            'all_news_list' : all_news_list
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
