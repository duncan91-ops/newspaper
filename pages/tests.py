from django.contrib.auth import get_user_model
from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve

from .views import HomePageView
from users.views import SignUpView


class HomePageTests(SimpleTestCase):

    def test_homepage_template(self):
        response = self.client.get('/')
        response_by_name = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_by_name.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
    
    def test_homepage_view(self):
        view = resolve('/')
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)


class SignupPageTests(TestCase):

    username = 'newuser'
    email = 'newuser@email.com'

    def test_signup_template(self):
        response = self.client.get('/users/signup/')
        response_by_name = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_by_name.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')
    
    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(
            self.username, self.email
        )
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)
