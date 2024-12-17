from django.db import models
from basic_app.models.base import BaseModel
from django.utils.translation import gettext_lazy as _

class Youtube(BaseModel):
    """YouTube news model"""
    url = models.URLField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Время создания
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = "youtube"
        managed = True
        verbose_name = _("YouTube")
        verbose_name_plural = _("YouTube")

    def __str__(self):
        return f"{self.pk} | {self.url[:30]}"