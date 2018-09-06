from django.db import models
from blog.models import Post
from django.contrib.auth.models import User

# Create your models here.
class Comment(models.Model):
    STATUS_SHOW = 1
    STATUS_ITEMS = (
        (1, '展示'),
        (2, '下线'),
    )
    # 内容管理系统, 时间非常重要, 什么时间产生, 什么时间删除, 被谁删除, 被谁创建
    # post = models.ForeignKey(Post, verbose_name='文章')
    target = models.CharField(max_length=200, null=True, verbose_name="评论目标")
    content = models.CharField(max_length=2000, verbose_name="内容")
    nickname = models.CharField(max_length=50, verbose_name="昵称")
    website = models.URLField(verbose_name="网站")
    email = models.EmailField(verbose_name='邮箱')
    status = models.PositiveIntegerField(default=STATUS_SHOW, choices=STATUS_ITEMS, verbose_name="状态")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")


    
    def post_name(self):
        return self.post.title
    post_name.short_description = '文章标题'
    
    class Meta:
        verbose_name = verbose_name_plural = "评论"
    


