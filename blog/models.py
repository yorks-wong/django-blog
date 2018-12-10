from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import markdown
from django.utils.html import strip_tags

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

    #统计浏览量
    views = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.title
    
    # 自定义 get_absolute_url 方法，使Post生成自己的URL
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def save(self, *args, **kwargs):    
        # 如果没有填写摘要
        if not self.excerpt:
            # 首先实例化一个 Markdown 类，用于渲染 body 的文本
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            # 先将 Markdown 文本渲染成 HTML 文本
            # strip_tags 去掉 HTML 文本的全部 HTML 标签
            # 从文本摘取前 54 个字符赋给 excerpt
            self.excerpt = strip_tags(md.convert(self.body))[:54]

        # 调用父类的 save 方法将数据保存到数据库中
        super(Post, self).save(*args, **kwargs)
