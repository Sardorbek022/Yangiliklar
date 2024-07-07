from django.urls import path

from .views import (
    HomePageView, ContactPageView, NewsDetailPage, CategoryDetailPage
)


urlpatterns = [
    path('', view=HomePageView.as_view(), name='home_page'),
    path('contact/', view=ContactPageView.as_view(), name='contact_page'),
    # path('news-detail/<int:pk>/', view=NewsDetailPage.as_view(), name='news_detail_page'),
    path('news/<slug:news>/', view=NewsDetailPage.as_view(), name='news_detail_page'),
    # path('category-detail/<int:pk>/', view=CategoryDetailPage.as_view(), name='category_detail_page'),
    path('category/<slug:category>/', view=CategoryDetailPage.as_view(), name='category_detail_page'),
]
