from django.shortcuts import render, redirect
from ..forms import PostForm, CommentForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ..models import Post



# Write
def write(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            
            return redirect('main:board')
    else:
        
        form = PostForm()
    return render(request, 'main/write.html', {"form": form})


# Detail
def detail(request, post_id):
    
    if request.method == "POST":
        form = CommentForm(request.POST)
        print(request.POST)
        for f in form:
            print(f.errors)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            _post = get_object_or_404(Post, pk=post_id)
            comment.post = _post
            comment.save()
            # return
        
    _post = Post.objects.get(id = post_id)
    _post.content = _post.content.split('\n')
    _post.comment = _post.comment_set.order_by('-created_at')
    
    return render(request, 'main/detail.html', {'post': _post})


# Post Modify
@login_required(login_url='main:login')
def post_modify(request, post_id):
    _post = get_object_or_404(Post, pk=post_id)
    if request.user != _post.user:
        messages.error(request, "수정권한이 없습니다.")
        return redirect('main:detail', post_id=post_id)
    
    if request.method == "POST":
        form = PostForm(request.POST, instance=_post)
        if form.is_valid():
            _post.save()
            return redirect('main:detail', post_id=post_id)
        
    form = PostForm(instance=_post)
    return render(request, 'main/write.html', {"form": form})


# Post Delete
@login_required(login_url='main:login')
def post_delete(request, post_id):
    _post = get_object_or_404(Post, pk=post_id)
    if request.user != _post.user:
        messages.error(request, "삭제권한이 없습니다.")
        return redirect('main:detail', post_id=post_id)
    _post.delete()
    return redirect('main:my_home')
