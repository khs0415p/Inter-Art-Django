from typing import Any, Dict
from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from .models import Post, Comment
from argon2 import PasswordHasher
import re

class JoinForm(forms.ModelForm):
    
    password2 = forms.CharField(
            required=True,
            max_length=15,
            label="비밀번호확인",
            widget=forms.PasswordInput(attrs={
                'placeholder': "확인용 비밀번호를 입력해주세요."
            })
    )
    
    class Meta:
        model = get_user_model()
        fields = ['username', 'password', 'password2', 'first_name', 'last_name', 'email', 'gender']
        
        
    def clean_username(self):
        username = self.cleaned_data.get('username')
        username_length = len(username)
        if self._meta.model.objects.filter(username=username).exists():
            raise ValidationError('중복된 아이디가 존재합니다.')
        
        if username_length > 4:
            
            if re.search('[0-9]+', username) and re.search('[a-zA-Z]+', username):
                if  not re.search('[~!@#$%^&*()_+|<>?:{}]', username):
                    return username
                
                else:
                    raise ValidationError('아이디는 특수문자를 사용하실 수 없습니다.')
            else:
                raise ValidationError('아이디는 영문과 숫자의 조합으로 설정할 수 있습니다.')
        
        else:
            raise ValidationError('아이디는 최소 5글자 이상으로 설정할 수 있습니다.')
        
    def clean_password2(self):
        password1 = self.data.get("password")
        password2 = self.data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("입력하신 비밀번호가 다릅니다.")
        
    
    def clean_password(self):
        password = self.cleaned_data.get('password')
        password_length = len(password)
        if password_length > 4:
            
            if re.search('[0-9]+', password) and re.search('[a-zA-Zㄱ-ㅎ]+', password) and re.search('[~!@#$%^&*()_+|<>?:{}]', password):
                hashed_password = PasswordHasher().hash(password=password)
                return hashed_password
            
            else:
                raise ValidationError('비밀번호는 문자, 숫자 및 특수문자의 조합으로 설정할 수 있습니다.')
            
        else:
            raise ValidationError('비밀번호는 최소 5글자 이상으로 설정할 수 있습니다.')
    
    def clean_gender(self):
        gender = self.cleaned_data.get("gender")
        if gender == "None":
            raise ValidationError("성별을 선택해주세요.")
        return gender
        
     
    def save(self, commit=True):
        user = super().save(commit)
        user.password = self.cleaned_data['password']
        if commit:
            user.save()
                
        return user
        
        
class LoginForm(forms.ModelForm):
    username = forms.CharField(
            required=True,
            max_length=15,
            widget=forms.TextInput(attrs={
                'placeholder': "아이디를 입력해주세요."
            })
    )
    
    password = forms.CharField(
            required=True,
            max_length=15,
            widget=forms.PasswordInput(attrs={
                'placeholder': "비밀번호를 입력해주세요."
            })
    )
    class Meta:
        model = get_user_model()
        fields = ['username', 'password']
        
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        
        try:
            user = self._meta.model.objects.get(username=username)
        except:
            raise ValidationError("아이디가 존재하지 않습니다.")
        
        try:
            PasswordHasher().verify(user.password, password)
        
        except:
            raise ValidationError("비밀번호가 일치하지 않습니다.")


class PostForm(forms.ModelForm): # ModelForm 은 장고 모델 폼
    class Meta: # 장고 모델 폼은 반드시 내부에 Meta 클래스 가져야 함
        model = Post
        fields = ['title', 'content', 'image']
        labels = {
            'title': '제목',
            'content': '내용',
            'image': '이미지',
        }
        
class CommentForm(forms.ModelForm):
    comment = forms.CharField(
            required=True,
            label='',
            widget=forms.TextInput(attrs={
                'placeholder': "댓글을 달아주세요."
            })
    )
    class Meta:
        model = Comment
        fields = ['comment']
        