#!/usr/bin/env/ python3
# -*- coding:utf-8 -*-
"""
@Project: drf_blog
@File  :serializers.py
@Author:zy7y
@Date  :2021/6/4 22:11
@Desc  : 序列化
"""

from rest_framework import serializers

from .models import Post, Category, Comment, Link, Setting


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


# 注意继承的父类是 A
class PostDetailSerializer(PostSerializer):
    # 渲染后的正文
    body_html = serializers.SerializerMethodField()
    # 渲染后的目录
    toc_html = serializers.SerializerMethodField()


    def get_body_html(self, obj):
        return obj.get_md()[0]

    def get_toc_html(self, obj):
        return obj.get_md()[1]

    class Meta:
        model = Post
        fields = "__all__"

        read_only = ["body_html", "toc_html"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class SettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setting
        fields = "__all__"


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = "__all__"