from typing import Any
from django.core.management.base import BaseCommand, CommandError, CommandParser
from app.models import Student

class Command(BaseCommand):
    help = "建立學生"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("--name", type=str,help="學生名字") #, required=True ,action="store_true"
        parser.add_argument("--phoneNumber", type=str)
        parser.add_argument("--email", type=str)
        return super().add_arguments(parser)
    
    def handle(self, *args: Any, **options: Any):
        name = options["name"]
        phoneNumber = options["phoneNumber"]
        email = options["email"]
        Student.objects.create(name=name, phoneNumber=phoneNumber, email=email)

        #if options["delete"]:
        #    poll.delete()

        self.stdout.write(self.style.SUCCESS(f'Create the student {name}'))

        # return super().handle(*args, **options)
# python manage.py create_student --name stu88 --phoneNumber 0907393393 --email zaq@gmail.com