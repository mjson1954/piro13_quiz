from django.urls import path
from . import views

app_name = 'quiz'

urlpatterns = [
    # 일단 test 가 메인 페이지
    path('', views.test),
    path('quiz/create/', views.quiz_create),
    path('quiz/quiz_list/', views.quiz_list),
    path('<int:pk>/delete/', views.delete_view, name='delete_view'),
    path('<int:pk>/solve/', views.solve_quiz, name='solve_quiz'),
    path('quiz/quiz_rank/', views.quiz_rank, name='quiz_rank'),

]