from django.shortcuts import render, redirect
from .models import Category, Course, Lesson
from django.views import View
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout

# Create your views here.
def index(request):
    courses = Course.objects.all()
    categories = Category.objects.all()
    context = {
        'courses': courses,
        'categories': categories
    }
    return render(request, 'index/index.html', context)


def get_course(request, course_id,):
    exact_course = Course.objects.get(id=course_id)
    lessons = Lesson.objects.filter(course=exact_course)
    context = {
        'course': exact_course,
        'lessons': lessons
    }
    return render(request, 'index/course.html', context)

def get_lesson(request, lesson_id):
    exact_lesson = Lesson.objects.get(id=lesson_id)
    context = {
        'lesson': exact_lesson
    }
    return render(request, 'index/lesson.html', context)


def get_category(request, category_id):
    exact_category = Category.objects.get(id=category_id)
    courses = Course.objects.filter(category=exact_category)
    context = {
        'courses': courses
    }
    return render(request, 'index/category.html', context)


def about(request):
    return render(request, 'index/about.html')


class Register(View):
    template_name = 'registration/register.html'


    def get(self, request):
        context = {'form': RegisterForm}
        return render(request, self.template_name, context)


    def post(self, request):
        form = RegisterForm(request.POST)

        if form.is_valid():
            username = form.clean_username()
            password2 = form.clean_password2()
            email = form.cleaned_data.get("email")
            user = User.objects.create_user(username, password=password2, email=email)
            user.save()
            login(request, user)
            return redirect('/')
        context = {'form': RegisterForm}
        return render(request, self.template_name, context)


def logout_view(request):
    logout(request)
    return redirect('/')






