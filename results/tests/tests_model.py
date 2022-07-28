from django.test import TestCase
from results.models import Result
from users.models import User
from rest_framework.authtoken.models import Token
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

        cls.user: User = User.objects.create_superuser(
            username=cls.username,
            email=cls.email,
            password=cls.password,
        )
        cls.user_token = Token.objects.create(user=cls.user)

        cls.data = {
            "concurso": 5000,
            "data": "2022-03-11",
            "bola1": 4,
            "bola2": 5,
            "bola3": 30,
            "bola4": 33,
            "bola5": 41,
            "bola6": 52
        }

        cls.result = Result.objects.create(**cls.data)

    def test_results_fields(self):
        self.assertIsInstance(self.result.concurso, int)
        self.assertEqual(self.result.concurso, self.data["concurso"])
        self.assertIsInstance(self.result.data, str)
        self.assertEqual(self.result.data, self.data["data"])
        self.assertIsInstance(self.result.bola1, int)
        self.assertEqual(self.result.bola1, self.data["bola1"])
        self.assertIsInstance(self.result.bola2, int)
        self.assertEqual(self.result.bola2, self.data["bola2"])
        self.assertIsInstance(self.result.bola3, int)
        self.assertEqual(self.result.bola3, self.data["bola3"])
        self.assertIsInstance(self.result.bola4, int)
        self.assertEqual(self.result.bola4, self.data["bola4"])
        self.assertIsInstance(self.result.bola5, int)
        self.assertEqual(self.result.bola5, self.data["bola5"])
        self.assertIsInstance(self.result.bola6, int)
        self.assertEqual(self.result.bola6, self.data["bola6"])
        self.assertIsInstance(self.result, Result)
        


