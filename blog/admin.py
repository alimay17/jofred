from django.contrib import admin
from .models import Post

# admin.site.register(Post)
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
  fieldsets = [
    (None, {'fields': ['title', 'published_date', 'text']}),
    ]
  list_display = ('title','created_date','published_date', 'author')
  list_filter = ['created_date', 'published_date']
  search_fields = ['title']


admin.site.register(Post, BlogAdmin)