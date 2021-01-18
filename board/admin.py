from django.contrib import admin
from .models import Board, Comment

# Register your models here.

class BoardAdmin(admin.ModelAdmin):
    list_display = ('title',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'writer', 'board')


admin.site.register(Board, BoardAdmin)
admin.site.register(Comment, CommentAdmin)