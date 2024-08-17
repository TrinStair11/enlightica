from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('course/<int:course_id>/', views.get_course, name='course'),
    path('category/<int:category_id>/', views.get_category, name='category'),
    path('register/', views.Register.as_view()),
    path('logout/', views.logout_view),
    path('lesson/<int:lesson_id>/', views.get_lesson, name='lesson'),
    path('about/', views.about, name='about'),
]