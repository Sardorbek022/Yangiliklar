from django.db.models import Sum
from django.contrib.contenttypes.models import ContentType
from hitcount.models import HitCount

from .models import (
    CategoryModel, NewsModel
)


def UniversalView(self,):
    news_content_type = ContentType.objects.get_for_model(NewsModel)
    category_list = CategoryModel.objects.all()
    latest_news_list = NewsModel.manager.all().order_by('-publish_time')[:6]
    hit_counts = HitCount.objects.filter(content_type=news_content_type) \
                                 .values('object_pk') \
                                 .annotate(total_views=Sum('hits')) \
                                 .order_by('-total_views')[:5]
    popular_posts_ids = [hit['object_pk'] for hit in hit_counts]
    popular_posts = NewsModel.objects.filter(id__in=popular_posts_ids).order_by('-publish_time')
    context = {
        'category_list' : category_list,
        'latest_news_list' : latest_news_list,
        'popular_posts' : popular_posts
    }
    return context

