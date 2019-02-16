# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from models import Blog
import json


# Create your views here.
def index(request):
    return render(request, 'index.html')


def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    print title, content
    Blog.objects.create(title=title, content=content)
    print 'test'
    return HttpResponse('OK')


def update(request):
    id = request.POST.get('id')
    title = request.POST.get('title')
    content = request.POST.get('content')
    blog_obj = Blog.objects.get(id=int(id))
    blog_obj.title = title
    blog_obj.content = content
    blog_obj.save()
    return HttpResponse('Update is NOT finished.')


def delete(request):
    id = request.POST.get('id')
    Blog.objects.filter(id=id).delete()
    return HttpResponse('OK')


def search(request):
    search_str = request.POST.get('search_str')
    # pagesize = request.POST.get('pagesize')
    # current_page = request.POST.get('current_page')
    # start = (current_page - 1) * pagesize + 1
    # end = current_page * pagesize + 1
    # blog_objs = Blog.objects.filter(title__icontains=search_str)[start:end]
    blog_objs = Blog.objects.filter(title__icontains=search_str)
    result = []
    for obj in blog_objs:
        result.append({
            'id': obj.id,
            'title': obj.title,
            'content': obj.content,
        })
    return HttpResponse(json.dumps(result))


def get_data(request):
    id = request.GET.get('id')
    if id:
        id = int(id)
        blogs = Blog.objects.filter(id=id)
    else:
        blogs = Blog.objects.all()
    # blog_items = [{'title':blog.title, 'content': blog.content} for blog in blogs]
    blog_items = []
    for blog in blogs:
        blog_items.append({'title': blog.title, 'content': blog.content, 'id': blog.id})
    return HttpResponse(json.dumps(blog_items))
