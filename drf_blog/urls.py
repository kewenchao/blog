from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from blog import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = routers.DefaultRouter()
router.register(r'posts', views.PostViewSet)
router.register(r'categorys', views.CategoryViewSet)
router.register(r'comments', views.CommentViewSet)
router.register(r'links', views.LinkViewSet)
router.register(r'settings', views.SettingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mdeditor/', include('mdeditor.urls')),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # jwt token
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
