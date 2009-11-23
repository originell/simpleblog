import datetime
from django.contrib import admin
from django.conf import settings
from django.contrib.comments.moderation import CommentModerator, moderator
from models import Entry, Category

COMMENTS = getattr(settings, 'COMMENTS', True)
COMMENTS_NOTIFICATION = getattr(settings, 'COMMENTS_NOTIFICATION', False)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(Category, CategoryAdmin)

if COMMENTS:
    class EntryModerator(CommentModerator):
        email_notification = COMMENTS_NOTIFICATION
        enable_field = 'enable_comments'
    moderator.register(Entry, EntryModerator)
    
    def enable_comments(modeladmin, request, queryset):
        queryset.update(enable_comments=True)
    enable_comments.short_description = 'Enable comments'

class EntryAdmin(admin.ModelAdmin):
    save_on_top = True
    list_per_page = 25
    list_display = ('title', 'created', 'modified')
    search_fields = ('title', 'body')
    date_hierarchy = 'created'

    prepopulated_fields = {'slug': ('title',)}

    if COMMENTS:
        actions = [enable_comments]

    def save_form(self, request, form, change):
        instance = form.save(commit=False)
        if not change:
            instance.created = datetime.datetime.now()
            instance.modified = instance.created
        else:
            instance.modified = datetime.datetime.now()

        return instance
admin.site.register(Entry, EntryAdmin)
