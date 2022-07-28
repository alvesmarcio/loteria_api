from users.models import User
from results.models import Result
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from faker import Faker


class ResultsViewTest(APITestCase):
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

    def test_result_create(self):
        data  = {
            "concurso": 6000,
            "data": "2022-05-12",
            "bola1": 4,
            "bola2": 15,
            "bola3": 35,
            "bola4": 39,
            "bola5": 41,
            "bola6": 52
        }

        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.user_token.key)

        response = self.client.post("/api/results/", data, format="json")
        self.assertEqual(response.data["concurso"], 6000)
        self.assertEqual(response.status_code, 201)

    def test_result_list(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.user_token.key)
        response = self.client.get("/api/results/")

        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data["results"]), 1)
        self.assertIsInstance(response.data["results"], list)

    def test_result_detail(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.user_token.key)
        response = self.client.get("/api/results/{}/".format(self.result.concurso))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["concurso"], self.result.concurso)

    def test_result_update(self):
        data = {
            "bola1": 1,
        }

        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.user_token.key)
        response = self.client.patch(
            "/api/results/{}/".format(self.result.concurso), data, format="json"
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["bola1"], data["bola1"])
        self.assertEqual(response.data["bola2"], self.result.bola2)
        

    def test_result_delete(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.user_token.key)
        response = self.client.delete("/api/results/{}/".format(self.result.concurso))

        self.assertEqual(response.status_code, 204)

    def test_result_detail_not_found(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.user_token.key)
        response = self.client.get("/api/results/{}/".format(9999))

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.data["detail"], "Not found.")
