from django import forms
from .models import Post

# PostForm은 사용자가 만들 폼의 이름
# 장고에게 PostForm이 ModelForm이라는 것을 알려줌
class PostForm(forms.ModelForm):
# class Meta 구문은 이 폼을 만들기 위해서 어떤 model이
# 쓰여야 하는지 장고에게 알려주는 구문이다.
    class Meta:
        model = Post
        fields = ('title', 'text',)
