from django.db import models
from django_quill.fields import QuillField
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from datetime import datetime
import os
from io import BytesIO
from PIL import Image, ImageOps
from django.core.files import File


class Status(models.TextChoices):
    published: str = "pub", _("Published")
    pending: str = "pen", _("Pending")


class CustomManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()


class BaseModel(models.Model):
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True,
        related_name='%(app_label)s_%(class)s_created_by', )
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL,
                                   blank=True, null=True, related_name='%(app_label)s_%(class)s_modified_by')

    objects = CustomManager()

    class Meta:
        abstract = True


class AbstractTemplate(BaseModel):
    """ abstract template for news posts and ads """
    image = models.ImageField(verbose_name=_("Asosiy rasm"), upload_to="image/%Y-%m-%d/", blank=True, null=True)
    title = models.CharField(verbose_name=_("Sarlavha"), max_length=500, null=True)
    subtitle = models.CharField(verbose_name=_("Short title"), max_length=500, null=True)
    post = QuillField(verbose_name=_("To'liq mazmuni"), null=True, blank=True)
    status = models.CharField(verbose_name=_("status"), max_length=50, choices=Status.choices, default=Status.pending)
    slug = models.SlugField(max_length=50, verbose_name="slug", unique=True,
                            help_text=_("Majburyat tug'ulmasa tegmang"))
    post_viewed_count = models.IntegerField(default=0, verbose_name=_("Ko'rilganlik soni"), help_text=_("Tegilmasin !"))
    author_post = models.CharField(verbose_name=_("Muallifi"), max_length=300)
    created_at = models.DateTimeField(
        default=datetime.now,  # Если значение не указано, будет использоваться текущее время
        verbose_name="Время создания"
    )
    updated_at = models.DateTimeField(
        default=datetime.now,  # Если значение не указано, будет использоваться текущее время
        verbose_name="Время обновления"
    )


    def save(self, *args, **kwargs):
        if self._state.adding:
            im = Image.open(self.image)
            im = im.convert('RGB')
            im = ImageOps.exif_transpose(im)
            im_io = BytesIO()
            im.save(im_io, 'JPEG', quality=50)
            filename = os.path.splitext(self.image.name)[0]
            filename = f"{filename}.jpg"
            new_image = File(im_io, name=filename)
            self.image = new_image
            super().save(*args, **kwargs)
            self.created_at = self.created_at or datetime.now()

        else:
            super().save(*args, **kwargs)
        self.updated_at = self.updated_at or datetime.now()
        super().save(*args, **kwargs)
    class Meta:
        abstract = True
        managed = True
