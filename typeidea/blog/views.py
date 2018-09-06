from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Post, Category, Tag
from comment.models import Comment
from config.models import SideBar
from comment.forms import CommentForm
from django.core.paginator import Paginator, EmptyPage
from django.views.generic import ListView, DetailView
from comment.views import CommentShowMixin

# Create your views here.
class CommonMixin(object):
    def get_category_context(self):
        categories = Category.objects.filter(status=1)
        nav_cates = []
        cates = []
        for cate in categories:
            if cate.is_nav:
                nav_cates.append(cate)
            else:
                cates.append(cate)
        
        return {
            'nav_cates': nav_cates,
            'cates': cates,
        }
    
    def get_side_bars(self):
        return SideBar.objects.filter(status=1)

    def get_context_data(self, **kwargs):
        side_bars = SideBar.objects.filter(status=1)
        recently_posts = Post.objects.filter(status=1)[:10]
        # hot_posts = Post.objects.filter(status=1)[:10]
        recently_comments = Comment.objects.filter(status=1)

        kwargs.update({
            'side_bars': side_bars,
            'recently_posts':recently_posts,
            'recently_comments': recently_comments,
        })
        kwargs.update(self.get_category_context())
        return super(CommonMixin, self).get_context_data(**kwargs)


class BasePostView(CommonMixin, ListView):
    model = Post
    template_name = 'template/blog/list.html'
    context_object_name = 'posts'
    paginate_by = 3


class IndexView(BasePostView):
    def get_queryset(self):
        query = self.request.GET.get('query')
        qs = super(IndexView, self).get_queryset()
        if not query:
            return qs
        return qs.filter(title__icontains=query)  # select * from blog_post where title ilike '%query%'

    def get_context_data(self, **kwargs):
        query = self.request.GET.get('query')
        return super(IndexView, self).get_context_data(query=query)

class CategoryView(BasePostView):
    def get_queryset(self):
        qs = super(CategoryView, self).get_queryset()
        # 通过self.kwargs拿到url的参数
        cate_id = self.kwargs.get('category_id')
        qs = qs.filter(category_id=cate_id)
        return qs


class TagView(BasePostView):
    def get_queryset(self):
        tag_id = self.kwargs.get('tag_id')
        try:
            tag = Tag.objects.get(id=tag_id)
        except Tag.DoesNotExist:
            return []
        posts = tag.post_set.all()
        return posts


class PostView(CommonMixin, CommentShowMixin, DetailView):
    
    model = Post
    template_name = 'template/blog/detail.html'
    context_object_name = 'post'


class AuthorView(BasePostView):
    def get_queryset(self):
        author_id = self.kwargs.get('author_id')
        qs = super(AuthorView, self).get_queryset()
        if author_id:
            qs = qs.filter(owner_id=author_id)
        return qs
    


