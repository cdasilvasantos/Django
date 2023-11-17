from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import TodoList

class TodoListTest(TestCase):
    def setUp(self):
        # Create a user for authentication
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_create_record(self):
        # Authenticate the user
        self.client.login(username='testuser', password='testpassword')

        response = self.client.post(reverse('todo_create'), data={'this_item': 'value1', 'time': 'value2'})
        
        # Check if the record was created successfully
        self.assertEqual(response.status_code, 302)  # 302 indicates a successful redirect after creation
        self.assertEqual(TodoList.objects.count(), 1)  # Ensure that the record is in the database

    # ... (similar changes for other test methods)
