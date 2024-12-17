from django.contrib import admin
from django.utils.text import slugify

from basic_app.models import *


class BaseAdmin(admin.ModelAdmin):
    """
    Barcha admin modellar uchun umumiy funksiyalar:
    - `created_by` va `updated_by` maydonlarini avtomatik to'ldirish.
    - `slug` maydonini `title` dan avtomatik olish.
    """

    def save_model(self, request, obj, form, change):
        # `created_by` maydoni faqat yangi yozuv yaratilganda to'ldiriladi
        if not change or not obj.created_by:
            obj.created_by = request.user

        # `updated_by` maydoni har doim yangilanadi
        obj.updated_by = request.user

        # Agar `slug` bo'sh bo'lsa, `title` dan avtomatik yaratish
        if hasattr(obj, 'title') and hasattr(obj, 'slug') and not obj.slug:
            obj.slug = slugify(obj.title)

        super().save_model(request, obj, form, change)


class NewsAdmin(BaseAdmin):
    pass
class ElonAdmin(BaseAdmin):
    pass


class PostsAdmin(BaseAdmin):
    pass


class NavbarAdmin(BaseAdmin):
    pass


class AdministratorAdmin(BaseAdmin):
    pass


class InteractiveMapAdmin(BaseAdmin):
    pass
class YoutubeAdmin(BaseAdmin):
    pass

class BannerAdmin(BaseAdmin):
    pass

class TuzilmaAdmin(BaseAdmin):
    pass

class MaqsadAdmin(BaseAdmin):
    pass

class bolimAdmin(BaseAdmin):
    pass

admin.site.register(News, NewsAdmin)
admin.site.register(Elon, ElonAdmin)
admin.site.register(Posts, PostsAdmin)
admin.site.register(Navbar, NavbarAdmin)
admin.site.register(Administrator, AdministratorAdmin)
admin.site.register(InteractiveMap, InteractiveMapAdmin)
admin.site.register(Youtube, YoutubeAdmin)
admin.site.register(Banner, BannerAdmin)
admin.site.register(tuzilma, TuzilmaAdmin)
admin.site.register(maqsad, MaqsadAdmin)
admin.site.register(bolimlar, bolimAdmin)

