from django.contrib import admin
from .models import Publisher, Author, Book

# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name')


class BookAdmin(admin.ModelAdmin):
    # change list
    list_display = ('title', 'publisher', 'publication_date')
    list_filter = ('publication_date', )
    date_hierarchy = 'publication_date'
    ordering = ('-publication_date', )

    # edit fields # None = All

    # many to many rel form display
    filter_horizontal = ('authors', )

    # foreign key prettier select
    raw_id_fields = ('publisher', )


class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'state_province', 'website')
    list_filter = ('state_province', 'country')
    search_fields = ('name', )


admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
