from django.db import models
from django.contrib.auth.models import User
from django.utils.html import format_html
import markdown

# Create your models here.

# 分类
class Category(models.Model):
    STATUS_ITEMS = (
        (1, '正常'),
        (2, '删除')
    )
    # PositiveIntegerField 正数
    # BooleanField  bool值
    name = models.CharField(max_length=50, verbose_name='名称')
    status = models.PositiveIntegerField(default=1, choices=STATUS_ITEMS, verbose_name='状态')
    is_nav = models.BooleanField(default=False, verbose_name='是否导航')
    owner = models.ForeignKey(User, verbose_name="作者", on_delete=models.DO_NOTHING)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name = verbose_name_plural = '分类'

    def __str__(self):
        return self.name


# 标签
class Tag(models.Model):
    STATUS_ITMES = (
        (1, '正常'),
        (2, '删除'),
    )
    name = models.CharField(max_length=10, verbose_name='名称')
    status = models.PositiveIntegerField(default=1, choices=STATUS_ITMES, verbose_name='状态')
    owner = models.ForeignKey(User, verbose_name="作者", on_delete=models.DO_NOTHING)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = '标签'


# 文章
class Post(models.Model):
    STATUS_ITMES = (
        (1, '上线'),
        # (2, '草稿'),
        (3, '删除'),
    )
    title = models.CharField(max_length=255, verbose_name='标题')
    desc = models.CharField(max_length=1024, blank=True, verbose_name='摘要')
    content = models.TextField(verbose_name='正文', help_text="正文必须是markdown格式")
    html = models.TextField(verbose_name='渲染后的内容', default='', help_text="正文必须是markdown格式")
    is_markdown = models.BooleanField(verbose_name="使用markdown格式", default=True)
    status = models.PositiveIntegerField(default=1, choices=STATUS_ITMES, verbose_name='状态')
    # 类级属性(成员属性)
    category = models.ForeignKey('Category', verbose_name="分类")
    tag = models.ManyToManyField('Tag', verbose_name='标签')
    owner = models.ForeignKey(User, verbose_name='作者', on_delete=models.DO_NOTHING)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    # 自定义字段
    def show_status(self):
        return '当前状态:%s' %self.status
    show_status.short_description = '展示状态'


    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.is_markdown:
            config = {
                'codehilite': {
                    'use_pygments': False,
                    'css_class': 'prettyprint linenums',
                }
            }
            # self.html = markdown.markdown(self.content, extensions= ['codehilite'])
            self.html = markdown.markdown(self.content, extensions= ['codehilite'], extension_configs=config)
        # else:
        #     self.html = self.content
        return super(Post, self).save(*args, **kwargs)
    

    class Meta:
        verbose_name = verbose_name_plural = "文章"

    










    
    






