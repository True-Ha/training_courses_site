from django.core.management.base import BaseCommand

from users.bot.bot import executor

class Command(BaseCommand):

    def handle(self, *args, **options):
        executor()
