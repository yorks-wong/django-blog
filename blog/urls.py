from django.conf.urls import url
from . import views

app_name = 'blog'#视图函数命名空间，防止调用冲突
urlpatterns = [

    #绑定关系的写法是把网址和对应的处理函数作为参数传给 url 函数（第一个参数是网址，第二个参数是处理函数）
    #另外我们还传递了另外一个参数 name，这个参数的值将作为处理函数 index 的别名

    #匹配空字符串，调用首页函数index
    url(r'^$', views.index, name='index'),
    #匹配以 post/ 开头，后跟一个至少一位数的数字，并且以 / 符号结尾，调用文章详情视觉函数detail
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    #匹配形如/archives/2018/9/的网址
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
    #获取分类
    url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category'),
]
