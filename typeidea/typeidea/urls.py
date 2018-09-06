from django.conf.urls import include, url
from django.contrib import admin
from .custom_site import custom_site
from blog.views import  (IndexView, CategoryView,
 TagView, PostView, AuthorView)
from config.views import LinkView
from comment.views import CommentView

# from config.views import links


urlpatterns = [
    url(r'^$', IndexView.as_view(), name="index"),
    url(r'^category/(?P<category_id>\d+)/',CategoryView.as_view(), name="category"),
    url(r'^tag/(?P<tag_id>\d+)/$', TagView.as_view(), name="tag"),
    url(r'^post/(?P<pk>\d+)/$', PostView.as_view(), name="detail"),
    url(r'^author/(?P<author_id>\d+)/$', AuthorView.as_view(), name='author'),
    url(r'^links/$', LinkView.as_view(), name='link'),
    url(r'^comment/$', CommentView.as_view(), name='comment'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^cus_admin/', include(custom_site.urls)),
]

# urlpatterns = [
#     url(r'^$', post_list, name="index"),
#     url(r'^category/(?P<category_id>\d+)/', post_list, name="category"),
#     url(r'^tag/(?P<tag_id>\d+)/$', post_list, name="tag"),
#     url(r'^post/(?P<pk>\d+)/$', post_detail, name="detail"),
#     # url(r'^link/$', links),
#     url(r'^admin/', include(admin.site.urls)),
#     url(r'^cus_admin/', include(custom_site.urls)),
# ]
