from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email="artur@mail.ru",
            first_name="Admin",
            last_name="Store",
            is_staff=True,
            is_superuser=True,
        )

        user.set_password("0204artur")
        user.save()
