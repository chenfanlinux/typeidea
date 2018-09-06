from django.contrib import admin
from .models import SideBar, Link
from typeidea.custom_site import custom_site
from django.utils.html import format_html
from django.core.urlresolvers import reverse
# from .adminforms import PostAdminForm
from typeidea.custom_admin import BaseOwnerAdmin
# Register your models here.

@admin.register(SideBar, site=custom_site)
class SideBarAdmin(BaseOwnerAdmin):
    list_display = ['title', 'display_type', 'owner','status', 'created_time']


@admin.register(Link, site=custom_site)
class LinkAdmin(BaseOwnerAdmin):
    pass




