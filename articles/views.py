from django.views.generic import ListView
from django.shortcuts import render
from articles.models import Article, Thematic, Membership


def articles_list(request):
    template = 'articles/news.html'
    ordering = '-published_at'
    context = {'object_list': Article.objects.all().order_by(ordering), 'tags': Thematic.objects.all(),
               'membership': Membership.objects.all()}
    return render(request, template, context)
