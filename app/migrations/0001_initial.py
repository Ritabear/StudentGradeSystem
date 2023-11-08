# Generated by Django 4.2 on 2023-10-22 15:41

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Student",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=30, verbose_name="名字")),
                (
                    "phoneNumber",
                    models.IntegerField(
                        unique=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="請輸入正確的手機號碼", regex="^\\+?1?\\d{ㄚ,15}$"
                            )
                        ],
                        verbose_name="手機",
                    ),
                ),
                (
                    "email",
                    models.CharField(
                        max_length=50,
                        validators=[
                            django.core.validators.RegexValidator(
                                regex="\\w[\\w\\.-]*@\\w[\\w\\.-]+\\.\\w+"
                            )
                        ],
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Subject",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "subjectName",
                    models.CharField(max_length=30, unique=True, verbose_name="科目名稱"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Grade",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "semester",
                    models.CharField(
                        max_length=6,
                        validators=[
                            django.core.validators.RegexValidator(
                                regex="\\d{3}\\-[1-2]"
                            )
                        ],
                    ),
                ),
                (
                    "grade",
                    models.IntegerField(
                        blank=True,
                        null=True,
                        validators=[
                            django.core.validators.MaxValueValidator(100),
                            django.core.validators.MinValueValidator(0),
                        ],
                        verbose_name="成績",
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.student",
                        verbose_name="學生",
                    ),
                ),
                (
                    "subject",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.subject",
                        verbose_name="科目",
                    ),
                ),
            ],
        ),
    ]