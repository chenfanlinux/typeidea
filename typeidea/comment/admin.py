from django.contrib import admin
from .models import Comment
from typeidea.custom_site import custom_site
from django.utils.html import format_html
from django.core.urlresolvers import reverse
# from .adminforms import PostAdminForm
from typeidea.custom_admin import BaseOwnerAdmin
# Register your models here.

@admin.register(Comment, site=custom_site)
class CommentAdmin(BaseOwnerAdmin):
    list_display = ['target','nickname', 'website', 'email', 'status', 'created_time']
    # list_display = ['title', 'display_type', 'owner','status', 'created_time']

