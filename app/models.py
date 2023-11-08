from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator

import re


phoneNumberRule = RegexValidator(regex=r'^\+?1?\d{8,15}$',message="請輸入正確的手機號碼")
emailRule = RegexValidator(regex=r'\w[\w\.-]*@\w[\w\.-]+\.\w+',message="請輸入正確的email")
semesterRule = RegexValidator(regex=r'\d{3}\-[1-2]',message="請輸入正確的學期")


#學生
class Student(models.Model):
    name = models.CharField(verbose_name="名字",max_length=30,blank=False,null=False)
    phoneNumber = models.IntegerField(verbose_name="手機", blank=False,validators=[phoneNumberRule], unique=True)
    email =models.CharField(max_length=50,blank=False,validators=[emailRule])
    # gender = models.IntegerChoices(choices=((0, "男"), (1, "女"),(2,"未知")), default=2, verbose_name="性別")

    def __str__(self):
        return f"{self.name}"

    #Model 元資料就是"不是一個欄位的任何資料" -- 例如排序選項, admin 選項等等.
    class Meta:
        ordering = ['id'] #['-id']
        verbose_name = "學生"
        verbose_name_plural = verbose_name

#科目
class Subject(models.Model):
    subjectName = models.CharField(max_length=30,unique=True,verbose_name ="科目名稱")

    def __str__(self):
        return self.subjectName

    class Meta:
        verbose_name = "科目"
        verbose_name_plural = "科目"

# 成績
class Grade(models.Model):
    student = models.ForeignKey(verbose_name="學生", to=Student, on_delete=models.CASCADE, blank=False, null=False)
    semester = models.CharField(max_length=6, validators=[semesterRule])
    subject = models.ForeignKey(verbose_name="科目", to=Subject, on_delete=models.CASCADE, blank=False, null=False)
    grade = models.IntegerField(
        verbose_name="成績",
        validators=[MaxValueValidator(100), MinValueValidator(0)],
        blank=True,
        null=True
    )


    def __str__(self):
        return f"{self.student.name} on semester {self.semester} has {self.subject.subjectName} with grade {self.grade}"

    class Meta:
        verbose_name = "成績"
        verbose_name_plural = "成績"
        unique_together = ["student", "semester", "subject"]
