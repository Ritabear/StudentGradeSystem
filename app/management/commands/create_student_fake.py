from typing import Any
from django.core.management.base import BaseCommand, CommandError, CommandParser
from django.contrib.auth.hashers import make_password
from faker import Faker

from app.models import Student

class Command(BaseCommand):
    help = "建立 fake 學生"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('num', nargs='+', type=int)

    def handle(self, *args: Any, **options: Any):
        number = options.get('num')[0]   # 注意：此处options.get('num')是一个列表
        if number is None:
            number = 3
        # password = make_password('123456')
        faker = Faker(['zh_CN'])
        for _ in range(int(number)):
            data = {
                'name': faker.name_male(),
                'phoneNumber': faker.phone_number(),
                'email': faker.email(),
                # 'password': password,
                # 'is_superuser': True,
            }
            try:
                Student.objects.create(
                    **data
                )
                Student.save()
            except:
                CommandError('失敗！')
            self.stdout.write(self.style.SUCCESS(f'Successfully create user {faker.name_male()}'))
# python manage.py create_student_fake 3