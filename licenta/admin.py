from .models import Meals , Category
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.




class MealsAdmin(admin.ModelAdmin):  # instead of ModelAdmin

    list_display = ['name','category','price']
    search_fields = ['name', 'description']
    list_filter = ('category','people')


admin.site.register(Meals , MealsAdmin)
admin.site.register(Category)