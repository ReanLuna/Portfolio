from django.contrib import admin
from .models import Product
from .models import GraphicDesign
# Register your models here.


class ImageAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(Product)
admin.site.register(GraphicDesign, ImageAdmin)