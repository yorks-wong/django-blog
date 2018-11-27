from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Category(models.Model):#分类
    
    name = models.CharField(max_length=100)

    #定义一个__str__方法来优化返回数据
    def __str__(self):
        return self.name

class Tag(models.Model):#标签

    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Post(models.Model):#文章

    # 文章标题
    title = models.CharField(max_length=70)

    # 文章正文，使用 TextField 来存储大段文本。
    body = models.TextField()

    # 文章的创建时间和最后一次修改时间，存储时间的字段用 DateTimeField 类型。
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()

    # 文章摘要
    excerpt = models.CharField(max_length=200, blank=True)

    # 分类与标签
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)

    # 文章作者
    author = models.ForeignKey(User)
    
    def __str__(self):
        return self.title
    
    # 自定义 get_absolute_url 方法，使Post生成自己的URL
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})
