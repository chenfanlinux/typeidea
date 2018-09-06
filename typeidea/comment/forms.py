from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    # 隐藏target字段展示
    # target = forms.CharField(max_length=100, widget=forms.widgets.HiddenInput)
    nickname = forms.CharField(
        label = "昵称",
        max_length=50,
        widget = forms.widgets.Input(
            attrs={'class': "form-control"}
        )
    )
    email = forms.EmailField(
        label = "Email",
        max_length=50,
        widget = forms.widgets.EmailInput(
            attrs={'class': "form-control"}
        ) 
    )

    website = forms.URLField(
        label = "网站",
        max_length=50,
        widget = forms.widgets.URLInput(
            attrs={'class': "form-control"}
        ) 
    )
    content = forms.CharField(
        label = "内容",
        max_length=100,
        widget = forms.widgets.Textarea(
            attrs={'rows': 6, 'cols': 80, 'class': "form-control"}
        )
    )
    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) < 10:
            raise forms.ValidationError("长度怎么能这么短呢！！")
        return content

    class Meta:
        model = Comment
        fields = ['nickname', 'email', 'website', 'content']


