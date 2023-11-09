from typing import Any
from django.core.management.base import BaseCommand, CommandError, CommandParser
from django.contrib.auth.hashers import make_password
from faker import Faker

from app.models import Subject

class Command(BaseCommand):
    help = "建立 fake 科目"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('num', nargs='+', type=int)

    def handle(self, *args: Any, **options: Any):
        number = options.get('num')[0]
        if number is None:
            number = 3
        # password = make_password('123456')
        faker = Faker(['zh_TW'])
        for _ in range(int(number)):
            data = {
                'subjectName': faker.license_plate(),

            }
            try:
                Subject.objects.create(
                    **data
                )
                Subject.save()
            except Exception as e:
                self.stdout.write(f"{e}")
                CommandError('失敗！')
            self.stdout.write(self.style.SUCCESS(f'Successfully create user {faker.license_plate()}'))
            #! self.stdout.write vs print
# python manage.py create_Subject_fake 3