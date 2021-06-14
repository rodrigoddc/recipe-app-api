from django.test import TestCase

from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email(self):
        """Test creating a new user with an email is successful"""

        email = "a@a.com"
        password = "qwer1234"

        user = get_user_model().objects.create_user(
                                            email=email,
                                            password=password
                                            )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""

        email = 'qwer@QWER.com'

        user = get_user_model().objects.create_user(email,'qwer1234')

        self.assertEqual(user.email, email.lower())


    def test_new_user_invalid_email(self):
        """Test creating user with invalid email throws error"""

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'qwer1234')

    def test_create_super_user(self):
        """Test creating a new super user"""

        user = get_user_model().objects.create_superuser('qwer@qwer.com', 'qwer1234')

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

        return user
