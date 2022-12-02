from django.test import SimpleTestCase
from django.urls import reverse

class HomepageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    # def test_url_available_by_name(self):
    #     response = self.client.get(reverse("library-homepage"))
    #     self.assertEqual(response.status_code, 200)

    # def test_template_name_correct(self):
    #     response = self.client.get(reverse("library-homepage"))
    #     self.assertTemplateUsed(response, "elibrary/home.html")


class LoginpageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/login/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("login"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("login"))
        self.assertTemplateUsed(response, "users/loginpage.html")

class LogoutpageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.post("/logout/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.post(reverse("logout"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.post(reverse("logout"))
        self.assertTemplateUsed(response, "users/logout.html")

class RegisterpageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.post("/register/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.post(reverse("register"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.post(reverse("register"))
        self.assertTemplateUsed(response, "users/registerpage.html")


class AboutuspageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.post("/about/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("library-about"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("library-about"))
        self.assertTemplateUsed(response, "elibrary/about.html")