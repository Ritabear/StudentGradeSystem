from django.forms import ModelForm, forms
from app.models import Student, Subject, Grade

class CreateStudentForm(ModelForm):
    class Meta:
        # 這裡的model是指定要使用的model
        model = Student
        # 這裡的fields是指定要使用的欄位
        fields = "__all__"

# class CreateSubjectForm(forms.form):
class CreateSubjectForm(ModelForm):
    class Meta:
        model = Subject
        fields = "__all__"


class CreateGradeForm(ModelForm):
    class Meta:
        model = Grade
        fields = "__all__"
    # grade = forms.IntegerField(min_value=0, max_value=100)