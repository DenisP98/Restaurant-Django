from .models import Post , Category , Comment
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

class PostAdmin(admin.ModelAdmin):  # instead of ModelAdmin
  
    list_display = ['title' ,'author', 'category','created']
    search_fields = ['title', 'content']
    list_filter = ('category','tags')

admin.site.register(Post , PostAdmin)
admin.site.register(Category)
admin.site.register(Comment)