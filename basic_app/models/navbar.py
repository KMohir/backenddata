from django.db import models
from django.contrib.auth.models import User
from mptt.models import TreeForeignKey, MPTTModel
from django.utils.translation import gettext_lazy as _


class NavbarStatus(models.TextChoices):
    base = "base", _("Asosiy")
    inside = "inside", _("Ichki")


class Navbar(MPTTModel):
    """ Navigation bar model """
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True,
        verbose_name=_("object_make_user"), related_name="navbar_created_by"
    )
    name = models.CharField(verbose_name=_("Nomi"), max_length=100)
    parent = TreeForeignKey("self", related_name="children", on_delete=models.SET_NULL, null=True, blank=True)
    visible = models.BooleanField(default=True, verbose_name=_("Ko'rinish"))
    status = models.CharField(verbose_name=_("status"), max_length=30, choices=NavbarStatus.choices,
                              default=NavbarStatus.inside)
    order_num = models.IntegerField(verbose_name=_("Tartib raqami"), default=0)
    inside_order_num = models.IntegerField(default=0, verbose_name=_("Ichki tartib raqam"))
    slug = models.SlugField(max_length=120, unique=True)
    added_at = models.DateTimeField(auto_now_add=True)
    url = models.URLField(max_length=255, null=True, blank=True, help_text="Tegish shart emas")
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                    related_name="update_navbar_user")
    updated_at = models.DateTimeField(auto_now=True)

    class MPTTMeta:
        order_insertion_by = ("inside_order_num",)
        added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "navbar"
        managed = True
        ordering = ("order_num",)
        verbose_name = _("Bo'limlar")
        verbose_name_plural = _("Bo'limlar")

    def __str__(self):
        return self.name