from typing import Any, Dict
from django import forms
from .models import Member
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
import re


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'
        
    def clean_id(self):
        _id = self.cleaned_data.get('id')
        id_length = len(_id)
        
        if id_length > 4:
            
            if re.search('[0-9]+', _id) and re.search('[a-zA-Z]+', _id):
                if  not re.search('[~!@#$%^&*()_+|<>?:{}]', _id):
                    return _id
                
                else:
                    raise ValidationError('아이디는 특수문자를 사용하실 수 없습니다.')
            else:
                raise ValidationError('아이디는 영문과 숫자의 조합으로 설정할 수 있습니다.')
        
        else:
            raise ValidationError('아이디는 최소 5글자 이상으로 설정할 수 있습니다.')
        
    
    def clean_password(self):
        password = self.cleaned_data.get('password')
        password_length = len(password)
        if password_length > 4:
            
            if re.search('[0-9]+', password) and re.search('[a-zA-Z]+', password) and re.search('[~!@#$%^&*()_+|<>?:{}]', password):
                return password
            
            else:
                raise ValidationError('비밀번호는 영문, 숫자 특수문자 조합으로 설정할 수 있습니다.')
        
        else:
            raise ValidationError('비밀번호는 최소 5글자 이상으로 설정할 수 있습니다.')
        
        return
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        
        if re.match('^[a-zA_Z0-9+-_.]+@[a-zA_Z0-9]+\\.[a-zA_Z0-9-.]+$', email):
            if Member.objects.filter(email=email).exists():
                raise ValidationError('이미 가입된 이메일 입니다.')
            return email
        else:
            raise ValidationError('이메일 형식을 확인해주세요.')
        
class LoginForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['id', 'password']
        
    def clean(self):
        _id = self.cleaned_data.get('id')
        password = self.cleaned_data.get('password')
        
        if not password or not _id:
            raise ValidationError("아이디 또는 비밀번호를 입력해주세요.")
        
        try:
            member = Member.objects.get(id = _id)
        except:
            raise ValidationError("아이디가 존재하지 않습니다.")
        
        if (password != member.password):
            raise ValidationError("비밀번호가 일치하지 않습니다.")
        