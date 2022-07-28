from django.test import TestCase
from users.models import User
from faker import Faker
from user_numbers.models import UserNumbersModel


class UserNumbersModelTest(TestCase):
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

        cls.numbers = "14, 18"

        cls.user_numbers = UserNumbersModel.objects.create(
            user=cls.user,
            numbers=cls.numbers,
        )

    def test_user_number_fields(self):
        self.assertIsInstance(self.user_numbers.numbers, str)
        self.assertEqual(self.user_numbers.numbers, self.numbers)
