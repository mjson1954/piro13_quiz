from django.db import models
from django.forms.widgets import RadioSelect
from goologin import adapter

class Item(models.Model):
    CHOICES1 = [('1', '아리랑'), ('2', '아리랑'), ('3', '아리랑'), ('4', '아리랑'), ('5', '아리랑')]
    CHOICES2 = [('1', '아리랑'), ('2', '아리랑'), ('3', '아리랑'), ('4', '아리랑'), ('5', '아리랑')]
    CHOICES3 = [('1', '아리랑'), ('2', '아리랑'), ('3', '아리랑'), ('4', '아리랑'), ('5', '아리랑')]
    CHOICES4 = [('1', '아리랑'), ('2', '아리랑'), ('3', '아리랑'), ('4', '아리랑'), ('5', '아리랑')]
    CHOICES5 = [('1', '아리랑'), ('2', '아리랑'), ('3', '아리랑'), ('4', '아리랑'), ('5', '아리랑')]

    madeby = models.CharField(max_length=30, null=True)

    # 퀴즈 제목
    title = models.CharField(max_length=30, blank=True)
    # 퀴즈 5개 문제 정의 (~~~는? 영역)
    Q1 = models.CharField(max_length=60, blank=False)
    Q2 = models.CharField(max_length=60, blank=False)
    Q3 = models.CharField(max_length=60, blank=False)
    Q4 = models.CharField(max_length=60, blank=False)
    Q5 = models.CharField(max_length=60, blank=False)
    # 그냥 넣어야 할 거 같아서 넣었어..
    Q1pic = models.CharField(choices=CHOICES1, max_length=2, blank=False)
    Q2pic = models.CharField(choices=CHOICES2, max_length=2, blank=False)
    Q3pic = models.CharField(choices=CHOICES3, max_length=2, blank=False)
    Q4pic = models.CharField(choices=CHOICES4, max_length=2, blank=False)
    Q5pic = models.CharField(choices=CHOICES5, max_length=2, blank=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 퀴즈 제목 뽑아내기
    # def __str__(self):
    #     return self.title, self.madeby

    #  1차 마이그레이트


class Answer(models.Model):
    CHOICES1 = [('1', '아리랑'), ('2', '아리랑'), ('3', '아리랑'),
                ('4', '아리랑'), ('5', '아리랑')]
    CHOICES2 = [('1', '아리랑'), ('2', '아리랑'), ('3', '아리랑'),
                ('4', '아리랑'), ('5', '아리랑')]
    CHOICES3 = [('1', '아리랑'), ('2', '아리랑'), ('3', '아리랑'),
                ('4', '아리랑'), ('5', '아리랑')]
    CHOICES4 = [('1', '아리랑'), ('2', '아리랑'), ('3', '아리랑'),
                ('4', '아리랑'), ('5', '아리랑')]
    CHOICES5 = [('1', '아리랑'), ('2', '아리랑'), ('3', '아리랑'),
                ('4', '아리랑'), ('5', '아리랑')]

    item = models.ForeignKey(Item, related_name="answers", on_delete=models.CASCADE, null=True)
    madeby = models.CharField(max_length=30, null=True)

    Q1ans = models.CharField(choices=CHOICES1, max_length=2, blank=False)
    Q2ans = models.CharField(choices=CHOICES2, max_length=2, blank=False)
    Q3ans = models.CharField(choices=CHOICES3, max_length=2, blank=False)
    Q4ans = models.CharField(choices=CHOICES4, max_length=2, blank=False)
    Q5ans = models.CharField(choices=CHOICES5, max_length=2, blank=False)

