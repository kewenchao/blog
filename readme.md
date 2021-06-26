# 项目介绍
1. 学习drf 的实践项目，个人博客API

# 参考资料
1. https://www.django-rest-framework.org/
2. https://www.bilibili.com/video/BV1Sz4y1o7E8
3. https://www.cnblogs.com/zydeboke/p/11557875.html
4. https://www.dusaiphoto.com/article/115/
5. https://blog.csdn.net/weixin_34114823/article/details/89064055

# 功能
- [x] 登录 - django admin
- [x] 退出 - django admin
- [x] 文章
- [x] 分类
- [x] 友链
- [x] 设置
- [x] 权限认证 - django admin
**新增、编辑、修改接口加上django admin user 认证 只能在django admin 管理系统添加**

# 使用
1. python manage.py makemigrations blog
2. python manage.py migrate

3. python manage.py createsuperuser --email admin@example.com --username admin

4. python manage.py runserver

