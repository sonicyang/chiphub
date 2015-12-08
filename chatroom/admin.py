from django.contrib import admin

from chatroom.models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_filter = ['commenter', 'component', 'rank']
    list_display = ('pk', 'commenter','component', 'rank', 'text', 'date')
