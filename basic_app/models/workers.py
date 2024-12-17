from basic_app.models.base import *
from django.utils.translation import gettext_lazy as _


class Administrator(BaseModel):
    title = models.CharField(max_length=255, verbose_name=_("Lavozimi"))
    name = models.CharField(max_length=255, verbose_name=_("To'liq ismi"))
    position = models.CharField(max_length=255, verbose_name=_("Lavozimi"))
    phone = models.CharField(max_length=100, verbose_name=_("Telefon raqami"))
    image = models.ImageField(upload_to='administrators/')



    class Meta:
        db_table = 'administrators'
        verbose_name = _("Administrator")
        verbose_name_plural = _("Administrators")
