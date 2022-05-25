from django.test import TestCase
from django.contrib.auth import get_user_model


# Create your tests here.

class UserAccountTest(TestCase):

    def test_new_superuser(self):
        db = get_user_model()
        super_user = db.objects.create_superuser(
            'testuser@gmail.com', 'tester', 'password'
        )
        self.assertEqual(super_user.email, 'testuser@gmail.com')
        self.assertEqual(super_user.first_name, 'tester')
        self.assertTrue(super_user.is_active)
        self.assertEqual(str(super_user), 'testuser@gmail.com')

        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                '', 'tester', 'password'
            )
        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                'testuser@gmail.com', '', 'password'
            )
        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                'testuser@gmail.com', 'tester', ''
            )

    def test_new_user(self):
        db = get_user_model()
        user = db.objects.create_user(
            'testuser@gmail.com', 'tester', 'password'
        )
        self.assertEqual(user.email, 'testuser@gmail.com')
        self.assertEqual(user.first_name, 'tester')
        self.assertTrue(user.is_active)
        self.assertEqual(str(user), 'testuser@gmail.com')
        
        with self.assertRaises(ValueError):
            db.objects.create_user(
                '', 'tester', 'password'
            )
        with self.assertRaises(ValueError):
            db.objects.create_user(
                'testuser@gmail.com', '', 'password'
            )
        with self.assertRaises(ValueError):
            db.objects.create_user(
                'testuser@gmail.com', 'tester', ''
            )
