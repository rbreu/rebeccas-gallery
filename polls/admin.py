from polls.models import Poll, Choice
from django.contrib import admin

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

    
class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['published_at'], 'classes': ['collapse']}),
    ]
    list_display = ('question', 'published_at', 'was_published_today')
    inlines = [ChoiceInline]
    list_filter = ['published_at']
    search_fields = ['question']
    date_hierarchy = 'published_at'

admin.site.register(Poll, PollAdmin)
   
