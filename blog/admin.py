from django.contrib import admin
from blog.models import Article,Tag,Category
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title','create_time','modified_time','category','author']


admin.site.register(Article,ArticleAdmin)
admin.site.register(Category)
admin.site.register(Tag)