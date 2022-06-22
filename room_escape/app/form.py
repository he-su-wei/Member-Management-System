from django import forms
from django.forms import widgets


# class PostForm(forms.Form):
#     cNumber = forms.CharField(max_length=10, initial='')
#     cName = forms.CharField(max_length=10, initial='')
#     cMajor = forms.CharField(max_length=20, initial='')
#     cGrade = forms.CharField(max_length=1, initial='')
#     cPhone = forms.CharField(max_length=15, initial='')
#     cStatus = forms.CharField(max_length=15, initial='尚未進場')
CHOICES= (
('尚未進場', '尚未進場'),
('已進場', '已進場'),
)
year = (
('一', '一'),
('二', '二'),
('三', '三'),
('四', '四'),
)
Major= (
('健管系', '健管系'),
('保健系', '保健系'),
('醫暨系', '醫暨系'),
('心理系', '心理系'),
('視光系', '視光系'),
('聽語系', '聽語系'),
('物治系', '物治系'),
('職治系', '職治系'),
('護理系', '護理系'),
('生醫系', '生醫系'),
('資工系', '資工系'),
('商應系', '商應系'),
('資傳系', '資傳系'),
('經管系', '經管系'),
('休憩系', '休憩系'),
('會資系', '會資系'),
('財經系', '財經系'),
('財法系', '財法系'),
('外文系', '外文系'),
('社工系', '社工系'),
('幼教系', '幼教系'),
('數媒系', '數媒系'),
('視傳系', '視傳系'),
('商社系', '商社系'),
('時尚系', '時尚系'),
('室設系', '室設系'),
('物治系', '物治系'),
)

ctime = (
('前段17:30-18:30', '前段17:30-18:30'),
('前段18:10-19:10', '前段18:10-19:10'),
('中段18:50-19:50', '中段18:50-19:50'),
('中段20:30-21:30', '中段20:30-21:30'),
('後段21:10-22:10', '後段21:10-22:10'),
)

class PostForm(forms.Form):
    cNumber = forms.CharField(max_length=9, initial='')
    cName = forms.CharField(max_length=10, initial='')
    cMajor = forms.CharField(widget = widgets.Select(choices=Major))
    cGrade = forms.CharField(widget = widgets.Select(choices=year))
    ctime = forms.CharField(widget = widgets.Select(choices=ctime))
    cMail = forms.EmailField(max_length=35, initial='')
    cStatus = forms.CharField(widget = widgets.Select(choices=CHOICES))
