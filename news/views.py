from django.shortcuts import render
from django.views import View


class HomePageView(View):
    
    def get(self,request):
        return render(request=request, template_name='news/home.html')
    
    
class ContactPageView(View):
    
    def get(self, request):
        return render(request=request, template_name='news/contact.html')
    
    
class NewsDetailPage(View):
    
    def get(self, request):
        return render(request=request, template_name='news/news_detail.html')
    
    
class CategoryDetailPage(View):
    
    def get(self, request):
        return render(request=request, template_name='news/category_detail.html')
