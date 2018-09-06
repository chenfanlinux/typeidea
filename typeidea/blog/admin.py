from django.contrib import admin
from .models import Post, Category, Tag
from typeidea.custom_site import custom_site
from django.utils.html import format_html
from django.core.urlresolvers import reverse
from .adminforms import PostAdminForm
from typeidea.custom_admin import BaseOwnerAdmin
# Register your models here.

@admin.register(Post, site=custom_site)
class PostAdmin(BaseOwnerAdmin):

    # ---列表页面---

    # 列表字段
    form = PostAdminForm
    list_display = [
        'title', 'category', 'status', 'owner', 
        'created_time', 'show_status', 'operator'
    ]

    # list_display_links = ['category','status']

    # 过滤字段
    list_filter=['category', 'owner']

    # 搜索字段(外键增加)
    # search_fields = ['title', 'category__name', 'owner__username']
    search_fields = ['title', 'category__name']
    save_on_top = True

    # show_full_result_count = True
    actions_on_top = False
    actions_on_bottom = True
    # date_hierarchy = 'created_time'
    # list_editable = ('title', )

    # ---编辑页面---
    save_on_top = True

    # 布局
    fields = (
                ('category', 'title'), 
                'desc',
                'status',
                ('content', 'is_markdown'),
                'tag',
             )

    # fieldsets = (
    #     ('基础配置', {
    #         'fields': (
    #             ('category', 'title'), 
    #             'desc',
    #             'status',
    #             'content'
    #         )
    #     }
    #     ),

    #     ('高级配置', {
    #         'classes': ('collapse', 'addon'),
    #         'fields': ('tag', )
    #     }
    #     )
    # )
    
    # 标签过滤
    # filter_horizontal = ('tag', )

    # 增加编辑、删除操作
    def operator(self, obj):
        return format_html('<a href="{}">编辑</a>', 
                # '/cus_admin/blog/post/%s/' % obj.id
                reverse('cus_admin:blog_post_change', args=(obj.id,))
                )

    operator.short_description = "操作"



# class PostInlineAdmin(admin.TabularInline):
#     fields = ('title', 'status')
#     extra = 1  # 控制额外多几个
#     model = Post  # 文章


@admin.register(Category, site=custom_site)
class CategoryAdmin(BaseOwnerAdmin):
    # inlines = [
    #     PostInlineAdmin,
    # ]

    list_display = ['name', 'status', 'is_nav', 'created_time']
    fields = (
        'name', 'status',
        'is_nav',
    )


@admin.register(Tag, site=custom_site)
class TagAdmin(BaseOwnerAdmin):
    list_display = ['name', 'status', 'created_time']
    fields = (
        'name',
        'status'
    )
    
    
# admin.site.register(Post, PostAdmin)
# admin.site.register(Category, CategoryAdmin)
# admin.site.register(Tag, TagAdmin)
