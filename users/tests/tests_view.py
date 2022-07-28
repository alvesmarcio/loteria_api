from users.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from faker import Faker


class UserViewTest(APITestCase):
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

    def test_user_create(self):
        data = {
            "username": self.fake.user_name(),
            "email": self.fake.email(),
            "password": self.fake.password(),
        }

        response = self.client.post("/api/users/", data, format="json")
        self.assertEqual(response.status_code, 201)

    def test_user_list(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.user_token.key)
        response = self.client.get("/api/users/")

        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data), 1)

    def test_user_detail(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.user_token.key)
        response = self.client.get("/api/users/{}/".format(self.user.id))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["email"], self.user.email)

    def test_user_login(self):
        data = {
            "username": self.username,
            "password": self.password,
        }

        response = self.client.post("/api/login/", data, format="json")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "token")

    def test_user_update(self):
        data = {
            "email": self.fake.email(),
        }

        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.user_token.key)
        response = self.client.patch(
            "/api/users/{}/".format(self.user.id), data, format="json"
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["email"], data["email"])

    def test_user_delete(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.user_token.key)
        response = self.client.delete("/api/users/{}/".format(self.user.id))

        self.assertEqual(response.status_code, 204)
