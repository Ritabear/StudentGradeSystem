from django.contrib import admin

# Register your models here.
from .models import Student, Subject, Grade
# admin.site.register(Student)
# admin.site.register(Subject)
# admin.site.register(Grade)

# @admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    #  list_display = '__all__'
    list_display = ('name', 'gender','phoneNumber', 'email')
    list_filter = ['gender']
    search_fields = ['name','phoneNumber', 'email']

    ordering = ['id'] #-id
    # 每一個都要上去，fields與fieldsets兩者選一使用
    # fields =['name','gender','phoneNumber','email']
    fieldsets = (
        ('基本', {'fields': ['name', 'gender']}),
        ('高级', {
            'fields': ['phoneNumber', 'email'],
            'classes': ('collapse',)  # 是否折叠显示
        })
    )


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    pass

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    search_fields = ['student','semester','subject']
    #'autocomplete_fields[0]' must be a foreign key or a many-to-many field. and need to have 'search_fields' attribute set for student
    autocomplete_fields =['student']

admin.site.register(Student,StudentAdmin) #註冊至Administration(管理員後台)


admin.site.site_header = "學生成績管理系統"
admin.site.site_title = "成績管理系統"
admin.site.index_title = "歡迎使用成績管理系統"