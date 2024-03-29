from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, FormView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth import authenticate, login
from braces.views import LoginRequiredMixin

from django.contrib.auth.forms import UserCreationForm
from Accounts.forms import RegistrationForm
from .forms import CourseEnrollForm
from courses.models import Course
# Create your views here.
from Accounts.models import User

class StudentRegistrationView(CreateView):
    template_name = 'students/student/registration.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        result = super(StudentRegistrationView, self).form_valid(form)
        cd = form.cleaned_data
        user = authenticate(
               username=cd['username'],
               password=cd['password1']
               )
        # login(self.request, user)
        return result




class StudentEnrollCourseView(LoginRequiredMixin, FormView):
    course = None
    form_class = CourseEnrollForm

    def form_valid(self, form):
        print('hooo')
        self.course = form.cleaned_data['course']
        self.course.students.add(self.request.user)
        return super(StudentEnrollCourseView, self).form_valid(form)


    def get_success_url(self):
        return reverse_lazy('student:student_course_detail', args=[self.course.id])


class StudentCourseListView(LoginRequiredMixin, ListView):
    model = Course
    template_name = 'students/course/list.html'

    def get_queryset(self):
        print('entry')
        qs = super(StudentCourseListView, self).get_queryset()
        print(qs)
        return qs.filter(students__in=[self.request.user])


class StudentCourseDetailView(DetailView):
    model = Course
    template_name = 'students/course/detail.html'

    def get_queryset(self):
        print('entry')
        qs = super(StudentCourseDetailView, self).get_queryset()
        print(qs)
        return qs.filter(students__in=[self.request.user])

    def get_context_data(self, **kwargs):
            context = super(StudentCourseDetailView, self).get_context_data(**kwargs)
            # get course object
            course = self.get_object()
            if 'module_id' in self.kwargs:
                # get current module
                context['module'] = course.modules.get(
                    id=self.kwargs['module_id']
                )
            else:
                # get first module
                context['module'] = course.modules.all()[0]
            return context