from django.contrib import admin
from .models import Item, Answer
from .forms import QuizForm, AnswerForm

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['title']
    form = QuizForm



@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['madeby']
    form = AnswerForm
# Register your models here.
