from django.db import models

# Create your models here.
from mdeditor.fields import MDTextField


class Post(models.Model):
    title = models.CharField(max_length=200, null=False, verbose_name="文章标题")
    content = MDTextField(verbose_name="文章内容")
    status = models.IntegerField(default=1, name="文章状态,1 置顶显示 2正常显示 3 不显示", verbose_name="文章状态")
    reading = models.IntegerField(default=0, verbose_name="阅读量")
    created = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")
    updated = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = "文章管理"

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100, null=False, verbose_name="分类名称")
    created = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")
    updated = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        verbose_name = "分类"
        verbose_name_plural = "分类管理"

    def __str__(self):
        return self.name


class Link(models.Model):
    name = models.CharField(max_length=30, null=False, verbose_name="名称")
    path = models.CharField(max_length=255, null=False, verbose_name="链接")
    desc = MDTextField(verbose_name="描述")
    created = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")
    updated = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        verbose_name = "友链"
        verbose_name_plural = "友链管理"

    def __str__(self):
        return self.name


class Comment(models.Model):
    user = models.CharField(max_length=60, null=False, verbose_name="昵称")
    email = models.EmailField(verbose_name="邮箱", null=True)
    cr_id = models.ForeignKey('self', on_delete=models.CASCADE , null=True)
    pid = models.OneToOneField('Post', related_name='pid', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "评论"
        verbose_name_plural = "评论管理"

    def __str__(self):
        return self.user


class Setting(models.Model):
    name = models.CharField(max_length=100, null=False, verbose_name="网站标题")
    desc = MDTextField(verbose_name="网站描述")
    icon = models.FileField(upload_to='./media/', verbose_name="网站图标")
    start = models.TimeField(auto_now_add=True, verbose_name="网站开始运行时间")

    class Meta:
        verbose_name = "设置"
        verbose_name_plural = "系统设置"

    def __str__(self):
        return self.name
