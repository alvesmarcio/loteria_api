from django.test import TestCase
from users.models import User
from django.db import IntegrityError
from django.contrib.auth.models import AbstractUser
from faker import Faker


class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.fake = Faker()

        cls.username = cls.fake.user_name()
        cls.email = cls.fake.email()
        cls.password = cls.fake.password()

        cls.user: User = User.objects.create_user(
            username=cls.username,
            email=cls.email,
            password=cls.password,
        )

    def test_user_fields(self):
        self.assertIsInstance(self.user.email, str)
        self.assertEqual(self.user.email, self.email)

        self.assertIsInstance(self.user.username, str)
        self.assertEqual(self.user.username, self.username)

        self.assertIsInstance(self.user, AbstractUser)

    def test_unique_email(self):
        with self.assertRaises(IntegrityError):
            User.objects.create(
                username=self.username,
                email=self.email,
                password=self.password,
            )
