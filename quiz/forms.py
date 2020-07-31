from django import forms
from .models import Item
from .models import Answer


class QuizForm(forms.ModelForm):
    # 각 문제에 라디오 버튼 생성,
    #  모델폼 기능 구현을 위해 메타 클래스 생성 러브레터 참고자료에 모델 폼 있음
    class Meta:
        model = Item
        fields = '__all__'
        widgets = {
            'Q1pic': forms.RadioSelect,
            'Q2pic': forms.RadioSelect,
            'Q3pic': forms.RadioSelect,
            'Q4pic': forms.RadioSelect,
            'Q5pic': forms.RadioSelect,
        },


class AnswerForm(forms.ModelForm):
    # 각 문제에 라디오 버튼 생성,
    #  모델폼 기능 구현을 위해 메타 클래스 생성 러브레터 참고자료에 모델 폼 있음
    class Meta:
        model = Answer
        fields = '__all__'
        widgets = {
            'madeby': forms.CharField,
            'Q1ans': forms.RadioSelect,
            'Q2ans': forms.RadioSelect,
            'Q3ans': forms.RadioSelect,
            'Q4ans': forms.RadioSelect,
            'Q5ans': forms.RadioSelect,
        },


