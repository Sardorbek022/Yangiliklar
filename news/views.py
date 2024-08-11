from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.db.models import F, Sum
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from core.custom_permissions import OnlyLoggedSuperUser
from django.views.generic import ListView
from hitcount.models import HitCount
from django.contrib.contenttypes.models import ContentType
from hitcount.views import HitCountMixin
from django.views.generic import (
    UpdateView, DeleteView, CreateView
)
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import (
    NewsModel, ContactModel, CategoryModel
)

from .forms import (
    ContactForm, CommentForm
)


class HomePageView(LoginRequiredMixin, View):
    
    def get(self,request):
        all_news_list = NewsModel.manager.all().order_by('-publish_time')
        uzb_news_list = NewsModel.manager.all().filter(category__name="O'ZBEKISTON").order_by('-publish_time')[:6]
        world_news_list = NewsModel.manager.all().filter(category__name="JAHON").order_by('-publish_time')[:6]
        science_technology_news_list = NewsModel.manager.all().filter(category__name="FAN_TEXNIKA").order_by('-publish_time')[:6]
        sport_news_list = NewsModel.manager.all().filter(category__name="SPORT").order_by('-publish_time')[:6]
        
        context = {
            'all_news_list' : all_news_list,
            'uzb_news_list' : uzb_news_list,
            'world_news_list' : world_news_list,
            'science_technology_news_list' : science_technology_news_list,
            'sport_news_list' : sport_news_list,
        }

        return render(request=request, template_name='news/home.html', context=context)
    
    
class ContactPageView(LoginRequiredMixin, View):
    
    def get(self, request):
            return render(request=request, template_name='news/contact.html')
    
    
    def post(self, request):
        
        form = ContactForm(request.POST)
    
        if form.is_valid():
            form.save()
            return redirect('home_page')
            
        return render(request=request, template_name='news/contact.html', context={'form':form})
        
    
    
class NewsDetailPage(LoginRequiredMixin, HitCountMixin, View):
    
    def get(self, request, news):
        # news_detail = NewsModel.objects.get(pk=pk)
        # news_detail = get_object_or_404(NewsModel, pk=pk)
        news_detail = get_object_or_404(NewsModel, slug=news, status=NewsModel.Status.Active)
        # news_detail.view_count = news_detail.view_count + 1
        # news_detail.save()
        content_type = ContentType.objects.get_for_model(news_detail)
        hit_count, created = HitCount.objects.get_or_create(
            content_type=content_type,
            object_pk=news_detail.pk
        )

        # HitCountni yangilash
        self.hit_count(request, hit_count)

        # HitCount ob'ektini bazadan qayta yuklash, shunda yangilangan qiymatni to'g'ri ko'rinadi
        hit_count.refresh_from_db()

        comment_form = CommentForm()
        comments = news_detail.comments.filter(active=True)
        comment_count = comments.count()
        new_comment = None
        
        context = {
            'news_detail' : news_detail,
            'comments' : comments,
            'new_comment' : new_comment,
            'comment_form' : comment_form,
            'hit_count': hit_count.hits,
            'comment_count' : comment_count
        }
        
        return render(request=request, template_name='news/news_detail.html', context=context)
    
    def post(self, request, news):
        news_detail = get_object_or_404(NewsModel, slug=news, status=NewsModel.Status.Active)
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.news = news_detail
            new_comment.user = request.user
            new_comment.save()
            comment_form = CommentForm()
            return redirect(news_detail.get_absolute_url())
        else:
            # Agar forma noto'g'ri bo'lsa, xatoliklarni ko'rsatish
            context = {
                'news_detail': news_detail,
                'comments': news_detail.comments.filter(active=True),
                'new_comment': None,
                'comment_form': comment_form
            }
            return render(request, 'news/news_detail.html', context)


    
    
class CategoryDetailPage(LoginRequiredMixin, View):
    
    def get(self, request, category):
        
        # category_detail = NewsModel.objects.get(pk=pk)
        # category_detail = get_object_or_404(NewsModel, pk=pk)
        category_detail = get_object_or_404(CategoryModel, slug=category)
        category_news_list = NewsModel.manager.all().filter(category__name=category_detail).order_by('-publish_time')[:15]
        
        context = {
            'category_detail' : category_detail,
            'category_news_list' : category_news_list,
        }
        
        return render(request=request, template_name='news/category_detail.html', context=context)
    
    
class NewsUpdateView(OnlyLoggedSuperUser, UpdateView):
    
    model = NewsModel
    fields = ('title', 'body', 'image', 'category', 'status')
    template_name = 'crud/news_edit.html'
    
    def form_valid(self, form):
        news = form.save(commit=False)
        if news.status == NewsModel.Status.Deactive:
            news.save()
            return redirect('home_page')
        return super().form_valid(form)
    
    
class NewsDeleteView(OnlyLoggedSuperUser, DeleteView):
    
    model = NewsModel
    template_name = 'crud/news_delete.html'
    success_url = reverse_lazy('home_page')
    
    
class NewsCreateView(OnlyLoggedSuperUser, CreateView):
    
    model = NewsModel
    fields = ('title', 'slug', 'body', 'image', 'category', 'status')
    template_name = 'crud/news_create.html'


@login_required
@user_passes_test(lambda u:u.is_superuser)
def admin_page_view(request):

    admin_users = User.objects.filter(is_superuser=True)

    context = {
        'admin_users' : admin_users
    }

    return render(request=request, template_name='pages/admins.html', context=context)


class SearchResultsListView(LoginRequiredMixin, ListView):
    model = NewsModel
    template_name = 'news/search_result.html'
    context_object_name = 'all_news'

    def get_queryset(self):
        query = self.request.GET.get('q')
        
        return NewsModel.objects.filter(
            Q(title__icontains=query) | Q(body__icontains=query)
        )
