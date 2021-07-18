from django.contrib import admin
from app_news.models import New, Comment


class CommentInLine(admin.TabularInline):
    model = Comment


class NewsAdmin(admin.ModelAdmin):
    list_display = [
        'new_name',
        'new_create',
        'new_edit',
        'new_active_flag',
    ]
    list_filter = [
        'new_active_flag',
    ]
    inlines = [
        CommentInLine
    ]

    actions = [
        'mark_as_active',
        'mark_as_not_active',
    ]

    def mark_as_active(self, request, queryset):
        queryset.update(new_active_flag=True)

    def mark_as_not_active(self, request, queryset):
        queryset.update(new_active_flag=False)

    mark_as_active.short_description = 'Сделать статус новости Активная'
    mark_as_not_active.short_description = 'Сделать статус новости Неактивная'


class CommentAdmin(admin.ModelAdmin):
    list_display = [
        'user_name',
        'short_comment',
        'new',
    ]
    list_filter = [
        'user_name',
    ]

    actions = [
        'deleted_by_admin',
    ]

    @admin.display(description='Удалить комментарий')
    def deleted_by_admin(self, request, queryset):
        queryset.update(
            comment_text='"Удалено администратором"'
        )


admin.site.register(New, NewsAdmin)
admin.site.register(Comment, CommentAdmin)
