from users.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from faker import Faker
from user_numbers.models import UserNumbersModel


class UserNumberViewTest(APITestCase):
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
        cls.numbers = "14, 18"
        cls.user_numbers = UserNumbersModel.objects.create(
            user=cls.user,
            numbers=cls.numbers,
        )

        cls.test_user: User = User.objects.create_user(
            username=cls.fake.user_name(),
            email=cls.fake.email(),
            password=cls.fake.password(),
        )
        cls.test_user_token = Token.objects.create(user=cls.test_user)
        cls.test_numbers = "14, 20"

    def test_user_number_create(self):
        data = {
            "numbers": self.test_numbers,
        }
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.test_user_token.key)

        response = self.client.post("/api/numbers/", data, format="json")
        self.assertEqual(response.status_code, 201)

    def test_user_number_detail(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.user_token.key)

        response = self.client.get("/api/numbers/{}/".format(self.user_numbers.id))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["numbers"], self.numbers)

    def test_user_number_update(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.user_token.key)

        response = self.client.patch(
            "/api/numbers/{}/".format(self.user_numbers.id),
            {"numbers": self.test_numbers},
            format="json",
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["numbers"], self.test_numbers)

    def test_user_number_get_lucky(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.user_token.key)

        response = self.client.get("/api/numbers/")

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.data, list)
