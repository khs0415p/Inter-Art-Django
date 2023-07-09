from django.shortcuts import render, redirect
from ..forms import CommentForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ..models import Post, Comment



# Comment Modify
@login_required(login_url='main:login')
def comment_modify(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    
    if request.user != comment.user:
        messages.error("수정권한이 없습니다.")
        return redirect("main:detail", post_id=comment.post.id)
    
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save()
            return redirect("main:detail", post_id=comment.post.id)
    form = CommentForm(instance=comment)
    return render(request, 'main/comment_modify.html', {"form": form})


# Comment Delete
@login_required(login_url='main:login')
def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.user:
        messages.error(request, "삭제권한이 없습니다.")
        return redirect('main:detail', post_id=comment.post.id)
    comment.delete()
    return redirect('main:detail', post_id=comment.post.id)


# Like
@login_required(login_url='main:login')
def likes(request, post_id):
    
    _post = get_object_or_404(Post, pk=post_id)
    if _post.like_user.filter(pk=request.user.pk).exists():
        _post.like_user.remove(request.user)
    else:
        _post.like_user.add(request.user)
    
    return redirect(f'/main/detail/{post_id}')
