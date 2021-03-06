from django.urls import path
from . import views

app_name = 'discuss'
urlpatterns = [
    path('', views.index, name='index'),
    path('ask/', views.ask_question, name='ask_question'),
    path('tags/', views.tags_page, name='tags_page'),
    path('tags/<int:id>/', views.tag_questions, name='tag_questions'),
    path('<int:id>/', views.question_details, name='question_details')
]
