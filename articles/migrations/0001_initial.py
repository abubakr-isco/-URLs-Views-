from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=120, verbose_name="название")),
                ("slug", models.SlugField(allow_unicode=True, max_length=140, unique=True, verbose_name="адрес")),
            ],
            options={"verbose_name": "категория", "verbose_name_plural": "категории", "ordering": ["name"]},
        ),
        migrations.CreateModel(
            name="Article",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=200, verbose_name="заголовок")),
                ("text", models.TextField(verbose_name="текст")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="дата создания")),
                ("category", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="articles", to="articles.category", verbose_name="категория")),
            ],
            options={"verbose_name": "статья", "verbose_name_plural": "статьи", "ordering": ["-created_at", "-pk"]},
        ),
    ]
