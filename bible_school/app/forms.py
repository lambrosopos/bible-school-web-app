from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [ 'name', 'title', 'contact', 'memo' ]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "placeholder":"이름을 입력해주세요 (예: 홍길동)"
                }
            ),
            "title": forms.TextInput(
                attrs={
                    "placeholder":"현재 담당하고 있는 직책을 입력해주세요 (예: 권사)"
                }
            ),
            "contact": forms.TextInput(
                attrs={
                    "placeholder":"개인 연락처를 적어주세요 (예: 010-1234-4321)"
                }
            ),
            "memo": forms.Textarea(
                attrs={
                    "placeholder":"추가로 필요한 메모가 있다면 적어주세요"
                }
            )
        }
        labels = {
            "name": _("이름"),
            "title": _("직책"),
            "contact": _("연락처"),
            "memo": _("메모")
        }

