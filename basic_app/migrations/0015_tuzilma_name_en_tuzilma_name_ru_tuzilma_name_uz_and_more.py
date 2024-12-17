# Generated by Django 4.2.7 on 2024-12-08 18:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("basic_app", "0014_tuzilma"),
    ]

    operations = [
        migrations.AddField(
            model_name="tuzilma",
            name="name_en",
            field=models.CharField(
                max_length=255, null=True, verbose_name="To'liq ismi"
            ),
        ),
        migrations.AddField(
            model_name="tuzilma",
            name="name_ru",
            field=models.CharField(
                max_length=255, null=True, verbose_name="To'liq ismi"
            ),
        ),
        migrations.AddField(
            model_name="tuzilma",
            name="name_uz",
            field=models.CharField(
                max_length=255, null=True, verbose_name="To'liq ismi"
            ),
        ),
        migrations.AddField(
            model_name="tuzilma",
            name="position_en",
            field=models.CharField(max_length=255, null=True, verbose_name="Lavozimi"),
        ),
        migrations.AddField(
            model_name="tuzilma",
            name="position_ru",
            field=models.CharField(max_length=255, null=True, verbose_name="Lavozimi"),
        ),
        migrations.AddField(
            model_name="tuzilma",
            name="position_uz",
            field=models.CharField(max_length=255, null=True, verbose_name="Lavozimi"),
        ),
        migrations.AddField(
            model_name="tuzilma",
            name="title_en",
            field=models.CharField(max_length=255, null=True, verbose_name="Lavozimi"),
        ),
        migrations.AddField(
            model_name="tuzilma",
            name="title_ru",
            field=models.CharField(max_length=255, null=True, verbose_name="Lavozimi"),
        ),
        migrations.AddField(
            model_name="tuzilma",
            name="title_uz",
            field=models.CharField(max_length=255, null=True, verbose_name="Lavozimi"),
        ),
        migrations.CreateModel(
            name="maqsad",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("added_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=255, verbose_name="Lavozimi")),
                ("name", models.CharField(max_length=255, verbose_name="To'liq ismi")),
                ("position", models.CharField(max_length=255, verbose_name="Lavozimi")),
                (
                    "phone",
                    models.CharField(max_length=100, verbose_name="Telefon raqami"),
                ),
                ("image", models.ImageField(upload_to="administrators/")),
                (
                    "created_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="%(app_label)s_%(class)s_created_by",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "updated_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="%(app_label)s_%(class)s_modified_by",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "maqsad",
                "verbose_name_plural": "maqsad",
                "db_table": "maqsad",
            },
        ),
    ]