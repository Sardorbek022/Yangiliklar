from django.urls import path

from .views import (
    HomePageView, ContactPageView, NewsDetailPage, CategoryDetailPage
)


urlpatterns = [
    path('', view=HomePageView.as_view(), name='home_page'),
    path('contact/', view=ContactPageView.as_view(), name='contact_page'),
    path('news-detail/', view=NewsDetailPage.as_view(), name='news_deatail_page'),
    path('category-detail/', view=CategoryDetailPage.as_view(), name='category_deatail_page'),
]
