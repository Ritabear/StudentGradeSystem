from ast import List
from collections.abc import Sequence
from re import sub
import re
import stat
from typing import Any, Dict
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import (get_object_or_404, redirect,
                              render,
                              HttpResponseRedirect)

# Create your views here
from django.contrib import messages
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse, reverse_lazy
from app.models import Student, Subject, Grade
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from app.forms import CreateStudentForm, CreateSubjectForm, CreateGradeForm


def homePage(request):
    return render(request, "app/Base.html")

def index(request):
    return render(request, "app/Index.html")


def createSubject(request, pk=None):
    form = CreateSubjectForm(request.POST or None)
    # subjects = Subject.objects.all()
    if request.method == "POST":
        if 'save' in request.POST:
            form.save()
        # if 'update' in request.UPDATE:
        #     pk = request.POST.get('update')
        #     subject = Subject.objects.get(id=pk)
        #     form = CreateSubjectForm(request.POST, instance=subject)
        #     form.save()
        # elif 'delete' in request.POST:
        #     pk = request.POST.get('delete')
        #     subject = Subject.objects.get(id=pk)
        #     subject.delete()
    context = {
        "form": form,
    }
    #! sucess url
    return render(request, "app/CreateSubject.html", context=context)


def updateSubject(request, pk):
    # pass the object as instance in form
    obj = Subject.objects.get(id=pk)
    if request.method == "POST":
        form = CreateSubjectForm(request.POST, instance=obj)
        if form.is_valid():
            # print(form)
            form.save()

            context = {
                "subjects": Subject.objects.filter(id=pk),
            }
            print(context)

            return render(request, "app/SubjectListComponet.html", context=context)

            # 加上htmx 的 update form 會因為redirect 而有兩個nvibar
            # return redirect ('app:listSubjects')

    # add form dictionary to context
    context = {
        "form": CreateSubjectForm(),
        "subject": obj,
    }
    return render(request, 'app/UpdateSubject.html', context)


# def search(request, pk=None):
#     if request.method == "GET":
#         search_text = request.GET['search_text']
#     else:
#         search_text = ''
#     subjects = Subject.objects.filter(subjectName__contains=search_text)
#     context = {
#         "subjects": subjects
#     }
#     return render(request, 'app/Subject.html', context)
from django.db.models import Q


def searchStudent(request):
    name = request.POST.get("name", None)
    students = Student.objects.filter(Q(grade__semester__contains=name) | Q(name__contains=name))
    # semester = re.match(r'\d{3}\-[1-2]', name)
    # if semester:
    #     students = Student.objects.filter(Q(grade__semester__contains=semester) | Q(name__contains=False))
    # else:
    #     students = Student.objects.filter(name__contains=name)  if name else Student.objects.all()
    context = {
        "students": students,
    }
    return render(request, 'app/Search.html', context)


def searchComplete(request):
    name = request.GET.get("name", None)

    # if name:
    allInfo = Student.objects.filter(Q(grade__semester__contains=name) | Q(name__contains=name))
    return JsonResponse({"students": [i.name for i in allInfo]},status=200)

    # return render(request, 'app/Search.html')

# class ProductAutocomplete(View):
#     def get(self, request):
#         query = request.GET.get('term', '')
#         products = Product.objects.filter(name__icontains=query)[:10]
#         results = [product.name for product in products]
#         return JsonResponse(results, safe=False)


class ListGradeView(ListView):
    model = Grade
    template_name = 'app/Grade.html'
    context_object_name = "grades"

    # def get_context_data(self, **kwargs):#! overwite context_object_name
    #     pass


class CreateGradeView(CreateView):
    form_class = CreateGradeForm
    model = Grade
    template_name = 'app/CreateGrade.html'
    success_url = reverse_lazy('app:listGrades')


class UpdateGradeView(UpdateView):
    model = Grade
    fields = "__all__"
    template_name = 'app/UpdateGrade.html'
    success_url = reverse_lazy('app:listGrades')

    # def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
    #     context = super().get_context_data(**kwargs)
    #     context["headerNames"] = [subject.subjectName for subject in Subject.objects.all()]
    #     return context

    def form_valid(self, form):
        messages.success(self.request, "更改成功")
        return super().form_valid(form)


class DeleteGradeView(LoginRequiredMixin,DeleteView):
    model = Grade
    success_url = reverse_lazy('app:listGrades')
    template_name = 'DeleteGrade.html'


class ListStudentView(ListView):
    paginate_by = 9
    model = Student
    # template_name = 'templates/student.html'
    # templates 已經在settins 有定義了
    template_name = 'app/Student.html'
    context_object_name = "students"
    # paginate_by = 6
    # ordering = '-id'

    # def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
    #     context = super().get_context_data(**kwargs)
    #     context['path'] = self.request.path
    #     # print(self.kwargs)
    #     pk = self.kwargs['pk']
    #     return context


class CreateStudentView(CreateView):
    form_class = CreateStudentForm
    model = Student
    template_name = 'app/CreateStudent.html'
    # success_url = '/students'
    # success_url = reverse_lazy('app:createStudent')
    success_url = reverse_lazy('app:listStudents')

    # fields = "__all__"
    # fields = ["name","phoneNumber","email"] #?寫表單字段
    # context_object_name = "createStudents"
    #驗證表單
    # def form_valid(self, form):
    #     form.instance.created_by = self.request.user
    #     form.save()
    #     return redirect(self.success_url)


class UpdateStudentView(UpdateView):
    model = Student
    fields = "__all__"
    template_name = 'app/UpdateStudent.html'
    success_url = reverse_lazy('app:listStudents')

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["headerNames"] = [
            subject.subjectName for subject in Subject.objects.all()
        ]
        return context

    def form_valid(self, form):
        messages.success(self.request, "更改成功")
        return super().form_valid(form)


class DeleteStudentView(LoginRequiredMixin, DeleteView):
    model = Student
    success_url = reverse_lazy('app:listStudents')
    template_name = 'DeleteStudent.html'


# createSubject
class ListSubjectView(ListView):
    model = Subject
    template_name = 'app/Subject.html'
    context_object_name = "subjects"

    def get_ordering(self) -> Sequence[str]:
        ordering = self.request.GET.get('ordering', 'id')
        return [ordering]
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["SUBJECTS_API_URL"] = reverse_lazy("app:listSubjects")
        return context


class UpdateSubjectView(UpdateView):
    model = Subject
    fields = "__all__"
    template_name = 'app/UpdateSubject.html'
    success_url = reverse_lazy('app:listSubjects')





# ????
class DeleteSubjectView(LoginRequiredMixin,DeleteView):
    model = Subject
    # fields = "__all__"
    # fields = "id"
    # template_name = "DeleteSubject.html"  # 怎樣可以用subject.html
    template_name = "app/Subject.html"  # 怎樣可以用subject.html
    # success_url = reverse_lazy('get:app:listSubjects')
    success_url = reverse_lazy('app:listSubjects')

    def delete(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        # return HttpResponseRedirect(self.get_success_url())
        # AttributeError: 'DeleteSubjectView' object has no attribute 'object'
        return HttpResponse()

    def form_valid(self, form):
        messages.success(self.request, "The subject was deleted successfully.")
        return super().form_valid(form)

    #? FBV



#django.core.exceptions.ImproperlyConfigured: Using ModelFormMixin (base class of DeleteStudentView) without the 'fields' attribute is prohibited.
