from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from django.utils import timezone


def index(request):
    """Главная страница: выводит 5 последних опубликованных постов."""
    template_name = 'blog/index.html'
    post_list = Post.objects.filter(
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True
    ).order_by('-pub_date')[:5]
    context = {
        'post_list': post_list
    }
    return render(request, template_name, context)


def post_detail(request, id):
    """Страница отдельной публикации."""
    template_name = 'blog/detail.html'
    post = get_object_or_404(
        Post.objects.filter(
            pub_date__lte=timezone.now(),
            is_published=True,
            category__is_published=True
        ).select_related('category'),
        id=id
    )
    context = {
        'post': post
    }
    return render(request, template_name, context)


def category_posts(request, category_slug):
    """Страница категории: показывает посты выбранной категории."""
    template_name = 'blog/category.html'
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )

    post_list = Post.objects.filter(
        is_published=True,
        pub_date__lte=timezone.now(),
        category=category
    ).order_by('-pub_date')

    context = {
        'category': category,
        'post_list': post_list
    }
    return render(request, template_name, context)
