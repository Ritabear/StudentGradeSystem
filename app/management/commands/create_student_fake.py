import random
from typing import Any
from django.core.management.base import BaseCommand, CommandError, CommandParser
from django.contrib.auth.hashers import make_password
from django.db import transaction
from faker import Faker

from app.models import Student

#! django transaction
class Command(BaseCommand):
    help = "建立 fake 學生"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('num', nargs='+', type=int)

    def handle(self, *args: Any, **options: Any):
        number = options.get('num')[0]   #error: the following arguments are required: num
        # password = make_password('123456')
        faker = Faker(['zh_TW'])
        for _ in range(int(number)):
            data = {
                'name': faker.name_male(),
                'gender': random.randint(0, 2),
                'phoneNumber': str(faker.numerify('09########')), #phoneNumber:str
                'email': faker.email(),
                # 'password': "password",
                # 'is_superuser': True,
            }
            try:
                with transaction.atomic():
                    Student.objects.create(
                        **data
                    )
                # Student.save()
            except Exception as e:
                print(f"Error: {e}")
                raise CommandError(f'{e}') # 到這邊return 出去後面不會直接執行
            self.stdout.write(self.style.SUCCESS(f'Successfully create user {faker.name_male()}'))
            #! self.stdout.write vs print
# python manage.py create_student_fake 3