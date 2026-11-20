from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView
from .models import Article, Category


class ArticleListView(ListView):
    model = Article
    template_name = "articles/article_list.html"
    context_object_name = "articles"
    paginate_by = 5

    def get_queryset(self):
        queryset = Article.objects.select_related("category")
        query = self.request.GET.get("q", "").strip()
        if query:
            queryset = queryset.filter(title__icontains=query)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["q"] = self.request.GET.get("q", "").strip()
        context["categories"] = Category.objects.all()
        return context


class ArticleDetailView(DetailView):
    model = Article
    template_name = "articles/article_detail.html"
    context_object_name = "article"
    queryset = Article.objects.select_related("category")


class CategoryDetailView(ListView):
    model = Article
    template_name = "articles/category_detail.html"
    context_object_name = "articles"
    paginate_by = 5

    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs["slug"])
        return self.category.articles.select_related("category").all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = self.category
        return context
