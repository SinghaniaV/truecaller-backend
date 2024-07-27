from django.core.management.base import BaseCommand
from identities.models import Identity, Registered, RegisteredToSaved


class Command(BaseCommand):
    help = 'Populate the UserProfile model with initial data'

    def handle(self, *args, **kwargs):
        # Define initial data
        users_data = [{
                'first_name': 'John',
                'last_name': 'Doe',
                'email': 'john.doe@example.com',
                'phone':'1234567894',
                'is_spam': False
            }, {
                'first_name': 'Jane',
                'last_name': 'Smith',
                'phone':'1234567893',
                'email': 'jane.smith@example.com',
                'is_spam': True
            }, {
                'first_name': 'Alice',
                'last_name': 'Johnson',
                'phone':'1234567892',
                'email': 'alice.johnson@example.com',
                'is_spam': False
            }, {
                'first_name': 'Bob',
                'last_name': 'Brown',
                'phone':'1234567891',
                'email': 'bob.brown@example.com',
                'is_spam': True
            }]

        registered_users = [{
                'first_name': 'Vishal',
                'last_name': 'Singhania',
                'email': 'vishal.singhania@example.com',
                'phone':'1234567890',
            }]

        # Populate the database
        # for user_data in users_data:
        #     Identity.objects.create(**user_data)
        
        for registered in registered_users:
            Registered.objects.create(**registered)
