from django.contrib import admin
from images.models import Image, Tag, Tagging

class TaggingInline(admin.StackedInline):
    model = Tagging
    extra = 1


class TagInline(admin.ModelAdmin):
    inlines = [ TaggingInline ]


class ImageAdmin(admin.ModelAdmin):
    inlines = [ TaggingInline ]



admin.site.register(Image, ImageAdmin)
admin.site.register(Tag)
#admin.site.register(Tagging)
