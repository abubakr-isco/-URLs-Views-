from django.test import TestCase
from django.urls import reverse
from .models import Article, Category


class ArticlePageTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.category = Category.objects.create(name="Python", slug="python")
        cls.other_category = Category.objects.create(name="Django", slug="django")
        for number in range(7):
            Article.objects.create(title=f"Python article {number}", text="Article body", category=cls.category)
        cls.other = Article.objects.create(title="Django guide", text="Other body", category=cls.other_category)

    def test_detail_and_missing_article(self):
        response = self.client.get(reverse("article_detail", args=[self.other.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Django guide")
        self.assertEqual(self.client.get(reverse("article_detail", args=[99999])).status_code, 404)

    def test_search_and_pagination_preserve_query(self):
        response = self.client.get(reverse("article_list"), {"q": "PYTHON"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["articles"]), 5)
        self.assertContains(response, "q=PYTHON&amp;page=2")
        next_page = self.client.get(reverse("article_list"), {"q": "PYTHON", "page": 2})
        self.assertEqual(len(next_page.context["articles"]), 2)
        self.assertNotContains(next_page, "Django guide")

    def test_category_route_and_missing_category(self):
        response = self.client.get(reverse("category_detail", args=["python"]))
        self.assertEqual(len(response.context["articles"]), 5)
        self.assertContains(response, reverse("article_detail", args=[response.context["articles"][0].pk]))
        self.assertEqual(self.client.get(reverse("category_detail", args=["missing"])).status_code, 404)
