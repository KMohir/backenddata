# Generated by Django 4.2.7 on 2024-11-15 17:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("basic_app", "0003_news_subtitle_news_subtitle_en_news_subtitle_ru_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="navbar",
            old_name="update_user",
            new_name="updated_by",
        ),
        migrations.RemoveField(
            model_name="navbar",
            name="author",
        ),
        migrations.AddField(
            model_name="navbar",
            name="created_by",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="navbar_created_by",
                to=settings.AUTH_USER_MODEL,
                verbose_name="object_make_user",
            ),
        ),
        migrations.AlterField(
            model_name="news",
            name="subtitle",
            field=models.CharField(
                max_length=500, null=True, verbose_name="Short title"
            ),
        ),
        migrations.AlterField(
            model_name="news",
            name="subtitle_en",
            field=models.CharField(
                max_length=500, null=True, verbose_name="Short title"
            ),
        ),
        migrations.AlterField(
            model_name="news",
            name="subtitle_ru",
            field=models.CharField(
                max_length=500, null=True, verbose_name="Short title"
            ),
        ),
        migrations.AlterField(
            model_name="news",
            name="subtitle_uz",
            field=models.CharField(
                max_length=500, null=True, verbose_name="Short title"
            ),
        ),
        migrations.AlterField(
            model_name="posts",
            name="subtitle",
            field=models.CharField(
                max_length=500, null=True, verbose_name="Short title"
            ),
        ),
        migrations.AlterField(
            model_name="posts",
            name="subtitle_en",
            field=models.CharField(
                max_length=500, null=True, verbose_name="Short title"
            ),
        ),
        migrations.AlterField(
            model_name="posts",
            name="subtitle_ru",
            field=models.CharField(
                max_length=500, null=True, verbose_name="Short title"
            ),
        ),
        migrations.AlterField(
            model_name="posts",
            name="subtitle_uz",
            field=models.CharField(
                max_length=500, null=True, verbose_name="Short title"
            ),
        ),
    ]