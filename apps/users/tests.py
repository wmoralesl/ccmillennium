from django.test import TestCase
from users.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from datetime import date

class UserModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            first_name="Juan",
            last_name="Pérez",
            second_last_name="Gómez",
            role="student",
        )

    def test_username_autogenerado(self):
        self.assertIsNotNone(self.user.username)
        self.assertGreater(len(self.user.username), 0)

    def test_password_por_defecto(self):
        self.assertTrue(self.user.check_password(self.user.username))  # set_password usa hashing

    def test_get_full_name(self):
        nombre_completo = self.user.get_full_name()
        self.assertEqual(nombre_completo, "Juan Pérez Gómez")

    def test_soft_delete(self):
        self.user.delete()
        self.user.refresh_from_db()
        self.assertFalse(self.user.is_active)

    def test_cleanImg_elimina_foto(self):
        imagen = SimpleUploadedFile("test.jpg", b"file_content", content_type="image/jpeg")
        self.user.photo = imagen
        self.user.save()

        self.assertIsNotNone(self.user.photo)

        self.user.cleanImg()
        self.user.refresh_from_db()

        self.assertIsNone(self.user.photo)
