from django.contrib import admin

# Register your models here.
from .models import Post, Category, Comment, Link, Setting


# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     # 需要显示字段
#     list_display = ('title', 'category', 'reading', 'status', 'created')
#     # 每页数量 默认100条
#     list_per_page = 10
#     # 搜索字段
#     search_fields = ['title', 'category']
#     # 筛选字段
#     list_filter = ['created', 'status']
#
#
# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     # 需要显示字段
#     list_display = ('name', 'created')
#     # 每页数量 默认100条
#     list_per_page = 10
#     # 搜索字段
#     search_fields = ['name']
#     # 筛选字段
#     list_filter = ['created']
#
#
# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     # 需要显示字段
#     list_display = ('user', 'email', 'created')
#     # 每页数量 默认100条
#     list_per_page = 10
#     # 搜索字段
#     search_fields = ['user']
#     # 筛选字段
#     list_filter = ['created']
#
#
# @admin.register(Link)
# class LinkAdmin(admin.ModelAdmin):
#     # 需要显示字段
#     list_display = ('name', 'path', 'created')
#     # 每页数量 默认100条
#     list_per_page = 10
#     # 搜索字段
#     search_fields = ['name']
#     # 筛选字段
#     list_filter = ['created']
#
#
# @admin.register(Setting)
# class SettingAdmin(admin.ModelAdmin):
#     # 需要显示字段
#     list_display = ('name', 'start', 'created')
#     # 每页数量 默认100条
#     list_per_page = 10
#     # 搜索字段
#     search_fields = ['name']
#     # 筛选字段
#     list_filter = ['created']

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Link)
admin.site.register(Category)
admin.site.register(Setting)