from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField("название", max_length=120)
    slug = models.SlugField("адрес", max_length=140, unique=True, allow_unicode=True)

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"slug": self.slug})


class Article(models.Model):
    title = models.CharField("заголовок", max_length=200)
    text = models.TextField("текст")
    created_at = models.DateTimeField("дата создания", auto_now_add=True)
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, related_name="articles", verbose_name="категория"
    )

    class Meta:
        verbose_name = "статья"
        verbose_name_plural = "статьи"
        ordering = ["-created_at", "-pk"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"pk": self.pk})
