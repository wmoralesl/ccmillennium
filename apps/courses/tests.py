from django.test import TestCase
from courses.models import Course

class DummyTest(TestCase):
    def test_dummy(self):
        self.assertEqual(1 + 1, 2)

# Create your tests here.


class CoursesTestCase(TestCase):
    def setUp(self):
        
        Course.objects.create(name='Prueba')

    def test_correctName(self):
        objeto = Course.objects.get(name='Prueba')
        self.assertEqual(objeto.name, 'Prueba')