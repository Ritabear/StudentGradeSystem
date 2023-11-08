from typing import Any
from django.core.management.base import BaseCommand, CommandError, CommandParser
from django.db import transaction
from app.models import Student

class Command(BaseCommand):
    help = "刪除學生"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("--name", type=str,help="學生名字")

    # def handle(self, *args: Any, **options: Any) -> str | None:
    #     return super().handle(*args, **options)

    def handle(self, *args: Any, **options: Any):
        name = options["name"]
        # Student.objects.filter(name=name).delete()
        # self.stdout.write(self.style.SUCCESS(f'Delete the student {name}'))

        try:
            with transaction.atomic():
                students = Student.objects.filter(
                    name=name
                )

                if students.exists():
                    students.delete()
                else:
                    raise CommandError(f"{name} 該學生名稱不存在")
        except Exception as e:
            raise CommandError(e)
        self.stdout.write(self.style.SUCCESS(f" {name} successfully deleted"))

# python manage.py delete_student --name 黄玉兰