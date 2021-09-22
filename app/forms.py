from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [ 'name', 'title', 'contact', 'memo', 'church', 'cohort']
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "placeholder":"이름을 입력해주세요 (예: 홍길동)"
                }
            ),
            "title": forms.Select(
                attrs={
                    "placeholder":"현재 담당하고 있는 직책을 선택해주세요"
                    "(없는 경우에는 관리자에게 문의해주세요)"
                }
            ),
            "contact": forms.TextInput(
                attrs={
                    "placeholder":"(예시: 010-1234-4321)"
                }
            ),
            "church": forms.Select(
                attrs={
                    "placeholder":"현재 출석중인 계시는 교회를 선택해주세요"
                    "(없는 경우 관리자에게 문의해주세요)"
                }
            ),
            "cohort": forms.Select(
                attrs={
                    "placeholder":"등록할 기수를 선택해주세요"
                }
            ),
            "memo": forms.Textarea(
                attrs={
                    "placeholder":"추가로 필요한 메모가 있다면 적어주세요"
                }
            ),
        }
        labels = {
            "name": _("이름"),
            "title": _("직책"),
            "contact": _("연락처"),
            "church": _("교회"),
            "cohort": _("기수"),
            "memo": _("메모")
        }

