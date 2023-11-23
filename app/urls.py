from django.conf import settings
from django.urls import include,path

from django.conf.urls.static import static
from app import views
from app.views import ListStudentView,CreateStudentView,UpdateStudentView,DeleteStudentView, \
    ListGradeView,ListSubjectView,DeleteSubjectView,CreateGradeView,UpdateGradeView,DeleteGradeView,UpdateSubjectView
from django.conf.urls import handler403
# handler403 = 'app.views.custom_permission_denied'
# handler403 = views.permission_denied

app_name = "app"

urlpatterns = [
    path("", views.getIndex, name="index"),

    path("students/", views.ListStudentView.as_view(), name="listStudents"),
    path("studentsMore/", views.ListStudentView1.as_view(), name="listStudentsMore"),
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


    # path('students/search/', views.searchStudent, name='search'),
    # path('search/', views.searchStudent, name='search'),
    path('api/search/', views.searchComplete, name='searchComplete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)