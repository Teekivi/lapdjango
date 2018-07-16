from django.contrib import admin

from .models import Article

# Register your models here.


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "created_at")
    readonly_fields = ("author",)

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()
