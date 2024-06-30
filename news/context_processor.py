from .models import (
    CategoryModel, NewsModel
)


def UniversalView(self,):
    
    category_list = CategoryModel.objects.all()
    latest_news_list = NewsModel.manager.all().order_by('-publish_time')[:10]

    context = {
        'category_list' : category_list,
        'latest_news_list' : latest_news_list
    }
    return context

