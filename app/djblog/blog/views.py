""" Blog Views  """

from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from django.db.models import Prefetch
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.conf import settings
from django.core.cache import cache
from django.contrib.auth.models import User
from .models import Post, Tag
from .utils import ObjectDetailMixin, ObjectCreateMixin, ObjectUpdateMixin, ObjectDeleteMixin
from .forms import TagForm, PostForm



def posts_list(request):
    """ Get all posts with pagination """
    posts_cache = cache.get(settings.POSTS_CACHE_NAME)
    if posts_cache:
        posts = posts_cache
    else:
        posts = Post.objects.all().prefetch_related(
            Prefetch('tags', queryset=Tag.objects.all().only('title', 'slug')),
            Prefetch('user', queryset=User.objects.all().only('username'))
        )
        cache.set(settings.POSTS_CACHE_NAME, posts, settings.POSTS_CACHE_TIMEOUT)
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    is_paginated = page.has_other_pages()
    if page.has_previous():
        prev_url = f'?page={page.previous_page_number()}'
    else:
        prev_url = ''

    if  page.has_next():
        next_url = f'?page={page.next_page_number()}'
    else:
        next_url = ''
    context = {
        'page_object': page,
        'is_paginated': is_paginated,
        'prev_url': prev_url,
        'next_url': next_url
    }
    return render(request, 'blog/index.html', context)


class PostCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    """ Post create """
    form_model = PostForm
    template = 'blog/post_create_form.html'
    raise_exception = True


class PostDetail(ObjectDetailMixin, View):
    """ Post detail """
    model = Post
    template = 'blog/post_detail.html'


class PostUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    """ Post update """
    model = Post
    model_form = PostForm
    template = 'blog/post_update_form.html'
    raise_exception = True


class PostDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    """ Post delete """
    model = Post
    template = 'blog/post_delete_form.html'
    redirect_url = 'posts_list_url'
    raise_exception = True


def tags_list(request):
    """ Get all tags """
    tags = Tag.objects.all().prefetch_related(
            Prefetch('user', queryset=User.objects.all().only('username'))
            )
    return render(request, 'blog/tags_list.html', {'tags': tags})


class TagDetail(View):
    """ Tag detail """
    def get(self, request, slug):
        tag = get_object_or_404(Tag, slug__iexact=slug)
        post_with_tag = Post.objects.filter(tags=tag).prefetch_related(
            Prefetch('tags', queryset=Tag.objects.all().only('title', 'slug')),
            Prefetch('user', queryset=User.objects.all().only('username'))
            )
        paginator = Paginator(post_with_tag, 4)
        page_number = request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        is_paginated = page.has_other_pages()
        if page.has_previous():
            prev_url = f'?page={page.previous_page_number()}'
        else:
            prev_url = ''

        if  page.has_next():
            next_url = f'?page={page.next_page_number()}'
        else:
            next_url = ''
        context = {
            'page_object': page,
            'is_paginated': is_paginated,
            'prev_url': prev_url,
            'next_url': next_url,
            'tag': tag, 
            'admin': tag, 
            'detail': True
        }
        return render(request, 'blog/tag_detail.html', context)


class TagCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    """ Create tag class """
    form_model = TagForm
    template = 'blog/tag_create.html'
    raise_exception = True


class TagUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    """ Tag update """
    model = Tag
    model_form = TagForm
    template = 'blog/tag_update_form.html'
    raise_exception = True


class TagDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    """ Tag delete """
    model = Tag
    template = 'blog/tag_delete_form.html'
    redirect_url = 'tags_list_url'
    raise_exception = True
