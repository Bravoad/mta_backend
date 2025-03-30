from django.contrib import admin
from .models import Brand

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name_ru', 'is_displayed', 'order']
    search_fields = ['name_ru', 'name_en']
    list_filter = ['is_displayed']
    # Поле dynamic_description будет доступно в форме редактирования.
