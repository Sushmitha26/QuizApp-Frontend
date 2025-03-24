from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from django.urls import reverse
from .models import Question, Choice, Admin

class QuizAppTestCase(TestCase):
    def setUp(self):
        self.question = Question.objects.create(question="What is the capital of France?")
        Choice.objects.create(question=self.question, choice_text="Paris", is_correct=True)
        Choice.objects.create(question=self.question, choice_text="London", is_correct=False)

        Admin.objects.create(username="admin", password="password123")
        
        self.client = Client()

    def test_home_page(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_quiz_get(self):
        response = self.client.get(reverse('quiz'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.question.question)

    def test_quiz_post_correct_answer(self):
        correct_choice = self.question.choice_set.get(is_correct=True)
        response = self.client.post(reverse('quiz'), {
            f'choice{self.question.id}': correct_choice.id
        })
        self.assertContains(response, 'correct_answers')

    def test_admin_login_success(self):
        response = self.client.post(reverse('adminpage'), {
            'username': 'admin',
            'password': 'password123'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/actions.html')

    def test_admin_login_failure(self):
        response = self.client.post(reverse('adminpage'), {
            'username': 'admin',
            'password': 'wrongpassword'
        })
        self.assertRedirects(response, reverse('adminpage'))

    def test_create_quiz_view_get(self):
        response = self.client.get(reverse('create_quiz'))
        self.assertEqual(response.status_code, 200)
