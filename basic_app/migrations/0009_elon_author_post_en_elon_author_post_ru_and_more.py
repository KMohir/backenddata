# Generated by Django 4.2.7 on 2024-11-28 20:22

from django.db import migrations, models
import django_quill.fields


class Migration(migrations.Migration):

    dependencies = [
        ("basic_app", "0008_elon"),
    ]

    operations = [
        migrations.AddField(
            model_name="elon",
            name="author_post_en",
            field=models.CharField(max_length=300, null=True, verbose_name="Muallifi"),
        ),
        migrations.AddField(
            model_name="elon",
            name="author_post_ru",
            field=models.CharField(max_length=300, null=True, verbose_name="Muallifi"),
        ),
        migrations.AddField(
            model_name="elon",
            name="author_post_uz",
            field=models.CharField(max_length=300, null=True, verbose_name="Muallifi"),
        ),
        migrations.AddField(
            model_name="elon",
            name="post_en",
            field=django_quill.fields.QuillField(
                blank=True, null=True, verbose_name="To'liq mazmuni"
            ),
        ),
        migrations.AddField(
            model_name="elon",
            name="post_ru",
            field=django_quill.fields.QuillField(
                blank=True, null=True, verbose_name="To'liq mazmuni"
            ),
        ),
        migrations.AddField(
            model_name="elon",
            name="post_uz",
            field=django_quill.fields.QuillField(
                blank=True, null=True, verbose_name="To'liq mazmuni"
            ),
        ),
        migrations.AddField(
            model_name="elon",
            name="subtitle_en",
            field=models.CharField(
                max_length=500, null=True, verbose_name="Short title"
            ),
        ),
        migrations.AddField(
            model_name="elon",
            name="subtitle_ru",
            field=models.CharField(
                max_length=500, null=True, verbose_name="Short title"
            ),
        ),
        migrations.AddField(
            model_name="elon",
            name="subtitle_uz",
            field=models.CharField(
                max_length=500, null=True, verbose_name="Short title"
            ),
        ),
        migrations.AddField(
            model_name="elon",
            name="title_en",
            field=models.CharField(max_length=500, null=True, verbose_name="Sarlavha"),
        ),
        migrations.AddField(
            model_name="elon",
            name="title_ru",
            field=models.CharField(max_length=500, null=True, verbose_name="Sarlavha"),
        ),
        migrations.AddField(
            model_name="elon",
            name="title_uz",
            field=models.CharField(max_length=500, null=True, verbose_name="Sarlavha"),
        ),
    ]