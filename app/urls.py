from django.urls import include,path

from app import views
from app.views import ListStudentView,CreateStudentView,UpdateStudentView,DeleteStudentView, \
    ListGradeView,ListSubjectView,DeleteSubjectView,CreateGradeView,UpdateGradeView,DeleteGradeView,UpdateSubjectView

app_name = "app"

urlpatterns = [
    path("", views.index, name="index"),

    path("students/", views.ListStudentView.as_view(), name="listStudents"),
    path("students/create/", views.CreateStudentView.as_view(), name="createStudent"),
    # path("students/create", views.CreateStudentForm, name="createStudentForm"),
    path("students/update/<int:pk>/", views.UpdateStudentView.as_view(), name="updateStudents"),
    path("students/delete/<int:pk>/", views.DeleteStudentView.as_view(), name="deleteStudents"),
    # path("students/detail/<int:pk>", views.DetailStudentView.as_view(), name="detail_students"),

    path("grades/", views.ListGradeView.as_view(), name="listGrades"),
    path("grades/create/", views.CreateGradeView.as_view(), name="createGrade"),
    path("grades/update/<int:pk>/", views.UpdateGradeView.as_view(), name="updateGrades"),
    path("grades/delete/<int:pk>/", views.DeleteGradeView.as_view(), name="deleteGrades"),



    path("subjects/", views.ListSubjectView.as_view(), name="listSubjects"),
    path("subjects/create/", views.createSubject, name="createSubject"),

    path("subjects/update/<int:pk>/", views.updateSubject, name="updateSubjects"),
    # path("subjects/update/<int:pk>/", views.UpdateSubjectView.as_view(), name="updateSubjects"),

    # path("subjects/delete/<int:pk>", views.createSubject, name="deleteSubject"),
    path("subjects/delete/<int:pk>/", views.DeleteSubjectView.as_view(), name="deleteSubjects"),


    path('students/search/', views.searchStudent, name='search'),
    #re
    # path('search/', views.searchStudent, name='search'),
    path('api/search', views.searchComplete, name='searchComplete'),
]