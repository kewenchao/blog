from rest_framework import viewsets
from .models import Post, Comment, Category, Link, Setting
from .serializers import PostSerializer, CategorySerializer, CommentSerializer, LinkSerializer, SettingSerializer, \
    PostDetailSerializer

# 自定义装饰器 权限认证 登录用户才能进行部分接口访问
# https://blog.csdn.net/weixin_34114823/article/details/89064055
from functools import update_wrapper
from rest_framework.permissions import IsAdminUser


def wrap_permission(*permissions, validate_permission=True):
    """custom permissions for special route"""

    def decorator(func):
        def wrapper(self, request, *args, **kwargs):
            self.permission_classes = permissions
            if validate_permission:
                self.check_permissions(request)
            return func(self, request, *args, **kwargs)

        return update_wrapper(wrapper, func)

    return decorator


class IsVbAdminUser(IsAdminUser):
    """
    Allows access only to admin users.
    """

    def has_object_permission(self, request, view, obj):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        return self.has_permission(request, view)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # 配置过滤
    filter_fields = ('status',)

    def get_serializer_class(self):
        # 如果是查all 则 使用 一般的序列化数据
        if self.action == 'list':
            return PostSerializer
        else:
            # 查详细则使用 返回html的序列化器
            return PostDetailSerializer

    # 给create， update delete 请求加上权限

    @wrap_permission(IsVbAdminUser)
    def create(self, request, *args, **kwargs):
        # 创建接口
        return super(PostViewSet, self).create(request, *args, **kwargs)

    @wrap_permission(IsVbAdminUser)
    def update(self, request, *args, **kwargs):
        # 更新接口
        return super(PostViewSet, self).update(request, *args, **kwargs)

    @wrap_permission(IsVbAdminUser)
    def destroy(self, request, *args, **kwargs):
        # 删除接口
        return super(PostViewSet, self).destroy(request, *args, **kwargs)



class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @wrap_permission(IsVbAdminUser)
    def create(self, request, *args, **kwargs):
        # 创建接口
        return super(CategoryViewSet, self).create(request, *args, **kwargs)

    @wrap_permission(IsVbAdminUser)
    def update(self, request, *args, **kwargs):
        # 更新接口
        return super(CategoryViewSet, self).update(request, *args, **kwargs)

    @wrap_permission(IsVbAdminUser)
    def destroy(self, request, *args, **kwargs):
        # 删除接口
        return super(CategoryViewSet, self).destroy(request, *args, **kwargs)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    @wrap_permission(IsVbAdminUser)
    def update(self, request, *args, **kwargs):
        # 更新接口
        return super(CommentViewSet, self).update(request, *args, **kwargs)

    @wrap_permission(IsVbAdminUser)
    def destroy(self, request, *args, **kwargs):
        # 删除接口
        return super(CommentViewSet, self).destroy(request, *args, **kwargs)


class LinkViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer

    @wrap_permission(IsVbAdminUser)
    def create(self, request, *args, **kwargs):
        # 创建接口
        return super(LinkViewSet, self).create(request, *args, **kwargs)

    @wrap_permission(IsVbAdminUser)
    def update(self, request, *args, **kwargs):
        # 更新接口
        return super(LinkViewSet, self).update(request, *args, **kwargs)

    @wrap_permission(IsVbAdminUser)
    def destroy(self, request, *args, **kwargs):
        # 删除接口
        return super(LinkViewSet, self).destroy(request, *args, **kwargs)


class SettingViewSet(viewsets.ModelViewSet):
    queryset = Setting.objects.all()
    serializer_class = SettingSerializer

    @wrap_permission(IsVbAdminUser)
    def create(self, request, *args, **kwargs):
        # 创建接口
        return super(SettingViewSet, self).create(request, *args, **kwargs)

    @wrap_permission(IsVbAdminUser)
    def update(self, request, *args, **kwargs):
        # 更新接口
        return super(SettingViewSet, self).update(request, *args, **kwargs)

    @wrap_permission(IsVbAdminUser)
    def destroy(self, request, *args, **kwargs):
        # 删除接口
        return super(SettingViewSet, self).destroy(request, *args, **kwargs)
