from django.urls import path

from .views import (
    HomePageView, ContactPageView, NewsDetailPage, CategoryDetailPage, 
    NewsUpdateView, NewsDeleteView, NewsCreateView, admin_page_view, SearchResultsListView
)


urlpatterns = [
    path('', view=HomePageView.as_view(), name='home_page'),
    path('contact/', view=ContactPageView.as_view(), name='contact_page'),
    path('admin-page/', view=admin_page_view, name='admin_page'),
    # path('news-detail/<int:pk>/', view=NewsDetailPage.as_view(), name='news_detail_page'),
    path('news/<slug:news>/', view=NewsDetailPage.as_view(), name='news_detail_page'),
    # path('category-detail/<int:pk>/', view=CategoryDetailPage.as_view(), name='category_detail_page'),
    path('category/<slug:category>/', view=CategoryDetailPage.as_view(), name='category_detail_page'),
    path('news/<slug>/news-edit/', view=NewsUpdateView.as_view(), name='news_edit_page'),
    path('news/<slug>/news-delete/', view=NewsDeleteView.as_view(), name='news_delete_page'),
    path('news/<slug>/news-create/', view=NewsCreateView.as_view(), name='news_create_page'),
    path('searchresult/', view=SearchResultsListView.as_view(), name='search_result_page')
]
