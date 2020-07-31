from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Item, Answer
from .forms import QuizForm, AnswerForm


def test(request):
    return render(request, 'quiz/test.html')


def quiz_create(request, item=None):
    quizs = Item.objects.all()
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            item = form.save()
            return render(request, 'quiz/quiz_list.html', {'quizs': quizs})

    else:
        form = QuizForm()
    return render(request, 'quiz/item_form.html', {
        'form': form,
    })


def quiz_list(request):
    quizs = Item.objects.all()
    return render(request, 'quiz/quiz_list.html', {'quizs': quizs})


def delete_view(request, pk):
    context = {}
    quiz = Item.objects.get(pk=pk)
    quiz.delete()

    return render(request, 'quiz/delete_view.html', context)


def answer_quiz(request):
    quiz = Answer.objects.all()
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            item = form.save()
            return render(request, 'quiz/quiz_list.html', {'quiz': quiz})
    else:
        form = AnswerForm()
    return render(request, 'quiz/item_form.html', {
        'form': form,
    })


def solve_quiz(request, pk):
    quiz = Item.objects.get(pk=pk)
    answers = Answer.objects.all()
    if (request.method == 'POST'):
        form = AnswerForm(request.POST)
        if form.is_valid():
            item = form.save()
            return render(request, 'quiz/quiz_list.html', {'answers': answers, 'quiz':quiz})
    else:
        form = AnswerForm()
    return render(request, 'quiz/solve_quiz.html', {'form': form, 'quiz':quiz})


def quiz_rank(request):
    return render(request, 'quiz/quiz_rank.html')