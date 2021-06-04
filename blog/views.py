from rest_framework import viewsets
from .models import Post, Comment, Category, Link, Setting
from .serializers import PostSerializer, CategorySerializer, CommentSerializer, LinkSerializer, SettingSerializer, \
    PostDetailSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_serializer_class(self):
        # 如果是查all 则 使用 一般的序列化数据
        if self.action == 'list':
            return PostSerializer
        else:
            # 查详细则使用 返回html的序列化器
            return PostDetailSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class LinkViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer


class SettingViewSet(viewsets.ModelViewSet):
    queryset = Setting.objects.all()
    serializer_class = SettingSerializer

