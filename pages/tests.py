from django.test import TestCase, SimpleTestCase
from django.urls import reverse
# Create your tests here.

class HomepageTests(SimpleTestCase):
    def test_url_exist_at_correct_location(self):
        response = self.client.get("/")
        return self.assertEqual(response.status_code, 200)
    
    def test_url_available_by_name(self):
        response = self.client.get(reverse("home-page"))
        return self.assertEqual(response.status_code, 200)
    
    def test_template_name_correct(self):
        response = self.client.get(reverse("home-page"))
        return self.assertTemplateUsed(response, "home.html")
    
    def test_template_content(self):
        response = self.client.get(reverse("home-page"))
        return self.assertContains(response, "<h1>home page</h1>")
    
class AboutpageTests(SimpleTestCase):
    def test_url_exist_at_correct_location(self):
        response = self.client.get("/about/")
        return self.assertEqual(response.status_code, 200)
    
    
    def test_url_available_by_name(self):
        response = self.client.get(reverse("about-page"))
        return self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("about-page"))
        return self.assertTemplateUsed(response, "about.html")
    
    def test_template_content(self):
        response = self.client.get(reverse("about-page"))
        return self.assertContains(response, "<h1>about us!</h1>")