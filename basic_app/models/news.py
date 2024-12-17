from basic_app.models.base import *
from django.utils.translation import gettext_lazy as _


class News(AbstractTemplate):
    """ news """
    pdf_file = models.FileField(
        verbose_name=_("PDF fayl"), upload_to="pdf/news/%Y-%m-%d/",
        null=True, blank=True, help_text=_("Faqat *.pdf formatdagi faylarni yuklang")
    )
    video_file = models.FileField(
        verbose_name=_("Video fayl"), upload_to="videos/news/%Y-%m-%d/",
        null=True, blank=True, help_text=_("agar video fayl mavjud bo'lsa yuklang.")
    )

    class Meta:
        db_table = "news"
        managed = True
        verbose_name = _("Yangiliklar")
        verbose_name_plural = _("Yangiliklar")

    def __str__(self):
        return f"{self.pk} | {self.title[:30]}"
