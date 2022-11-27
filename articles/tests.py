from django.test import TestCase, SimpleTestCase
from django.urls import reverse

# Create your tests here.


class HomepageTest(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)


class AboutpageTest(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/articles/about/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)


class NewpageTest(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/articles/new/")
        self.assertEqual(response.status_code, 302)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("article_new"))
        self.assertEqual(response.status_code, 302)


class SearchpageTest(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/articles/search/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("search"))
        self.assertEqual(response.status_code, 200)
