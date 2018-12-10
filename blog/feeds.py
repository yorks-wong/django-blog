from django.contrib.syndication.views import Feed
from .models import Post


class AllPostsRssFeed(Feed):
    title = "Django Blog"
    link = "/"
    description = "Django Blog by yorks"
    def items(self):
        return Post.objects.all()
    def item_title(self, item):
        return '[%s] %s' % (item.category, item.title)
    def item_description(self, item):
        return item.body
