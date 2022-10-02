from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import CaruselModel


class CaruselAdm(admin.ModelAdmin):
    list_display = ('carusel_title', 'carusel_text', 'carusel_css', 'get_img')
    list_display_links = ('carusel_title',)
    list_editable = ('carusel_css',)
    fields = ('carusel_title', 'carusel_text', 'carusel_css', 'carusel_img', 'get_img')
    readonly_fields = ('get_img',)

    def get_img(self, obj):
        if obj.carusel_img:
            res = mark_safe(f'<img src="{obj.carusel_img.url}" width="80px" ')
        else:
            res = 'No image'
        return res
    get_img.short_description = "Image"


admin.site.register(CaruselModel, CaruselAdm)
