from django.test import TestCase
from django.urls import reverse
from myapp.models import Student
from .factories import StudentFactory

class StudentListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 10 Student objects
        for _ in range(10):
            StudentFactory.create()

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/students/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('student_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'myapp/student_list.html')

class StudentCreateViewTest(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/students/new/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('student_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'myapp/student_list.html')

    def test_create_student(self):
        post_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@example.com'
        }
        response = self.client.post(reverse('student_create'), post_data)
        self.assertEqual(response.status_code, 302)  # Redirect on success
        self.assertEqual(Student.objects.count(), 1)
        self.assertEqual(Student.objects.get().first_name, 'John')

class StudentUpdateViewTest(TestCase):
    def setUp(self):
        self.student = StudentFactory.create()

    def test_update_student(self):
        post_data = {
            'first_name': 'Jane',
            'last_name': 'Doe',
            'email': 'jane.doe@example.com'
        }
        url = reverse('student_update', kwargs={'pk': self.student.pk})
        response = self.client.post(url, post_data)
        self.assertEqual(response.status_code, 302)
        self.student.refresh_from_db()
        self.assertEqual(self.student.first_name, 'Jane')

class StudentDeleteViewTest(TestCase):
    def setUp(self):
        self.student = StudentFactory.create()

    def test_delete_student(self):
        url = reverse('student_delete', kwargs={'pk': self.student.pk})
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)  # Redirect on success
        self.assertEqual(Student.objects.count(), 0)
