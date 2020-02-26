from django.contrib import admin
from dev_up_api.models import Member, Board, Comment, Category, Tag, Photo

admin.site.register(Member)
admin.site.register(Category)
admin.site.register(Board)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(Photo)
