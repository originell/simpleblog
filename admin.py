import datetime
from django.contrib import admin
from models import Entry, Category

class CategoryAdmin(admin.ModelAdmin):

    list_display = ('name',)

admin.site.register(Category, CategoryAdmin)

class EntryAdmin(admin.ModelAdmin):

    save_on_top = True
    list_per_page = 25
    list_display = ('title', 'created', 'modified')
    search_fields = ('title', 'body')
    date_hierarchy = 'created'

    prepopulated_fields = {'slug': ('title',)}

    def save_form(self, request, form, change):
        instance = form.save(commit=False)
        if not change:
            instance.created = datetime.datetime.now()
        instance.modified = datetime.datetime.now()

        return instance

    def formfield_for_dbfield(self, db_field, **kwargs):
        field = super(EntryAdmin, self).formfield_for_dbfield(db_field,
                                                                **kwargs)
        if db_field.name == 'body':
            field.widget.attrs['class'] = 'vLargeTextField monospace'
        return field
admin.site.register(Entry, EntryAdmin)
