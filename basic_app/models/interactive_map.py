from basic_app.models.base import *
from django.utils.translation import gettext_lazy as _


class InteractiveMap(BaseModel):
    region_name = models.CharField(max_length=255, verbose_name=_("Viloyat nomi"))
    total_area = models.CharField(max_length=50, verbose_name=_("Umumiy maydon"))
    cultivated_area = models.CharField(max_length=50, verbose_name=_("Ekiladigan maydon"))
    forest_area = models.CharField(max_length=50, verbose_name=_("O'rmon xududi"))
    wasteland_area = models.CharField(max_length=50, verbose_name=_("Bosh yer hududi"))
    pastures_area = models.CharField(max_length=50, verbose_name=_("Yaylov xududi"))
    other_agricultural_land = models.CharField(max_length=50, verbose_name=_("Boshqa qishloq xojalik yerlari"))

    class Meta:
        db_table = 'regions_datas'
        verbose_name = _("Interactive Map")
        verbose_name_plural = _("Interactive Maps")

    def __str__(self):
        return f"{self.region_name}"
