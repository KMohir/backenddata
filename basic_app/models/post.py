from basic_app.models.base import *
from mptt.models import TreeForeignKey
from django.utils.translation import gettext_lazy as _


class Posts(AbstractTemplate):
    """ Posts """
    navbar = TreeForeignKey("Navbar", on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_("Bo'lim nomi"))
    pdf_file = models.FileField(
        verbose_name=_("PDF fayl"), upload_to="pdf/posts/%Y-%m-%d/",
        null=True, blank=True, help_text=_("Faqat *.pdf formatdagi faylarni yuklang")
    )
    video_file = models.FileField(
        verbose_name=_("Video fayl"), upload_to="videos/posts/%Y-%m-%d/",
        null=True, blank=True, help_text=_("agar video fayl mavjud bo'lsa yuklang.")
    )

    class Meta:
        db_table = "posts"
        managed = True
        verbose_name = _("Postlar")
        verbose_name_plural = _("Postlar")

    def __str__(self):
        return f"{self.navbar} | {self.title[:30]}"
