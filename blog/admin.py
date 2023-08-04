from django.contrib import admin
from blog.models import Post
# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'create_date'
    empty_value_display = '-empty-'
    list_display=('title', 'status', 'counted_views','published_at')
    list_filter=('status', )