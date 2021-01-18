from django.test import TestCase
import datetime
from task.models import InveraTask
from django.contrib.auth.models import User
from django.urls import reverse
from task.forms import FormNewTask

# Create your tests here.
class InveraTaskFormTest(TestCase):

    @classmethod
    def setUp(self):
        self.myuser1 = User.objects.create_user(username='Administrador 1', password='admin123', email='test@example.com')
        self.myuser2 = User.objects.create_user(username='Administrador 2', password='admin123', email='test1@test.com')
        dToday = datetime.date.today()
        Invera1 = InveraTask.objects.create(idTask=1, userTask=self.myuser1, title='Crear registro de usuarios', description='Crear registro con redes sociales',
            completed='False', created=dToday)
        Invera2 = InveraTask.objects.create(idTask=2, userTask=self.myuser2, title='Usar con docker', description='Terminar con docker',
            completed='True', created=dToday)

    def test_valid_form_data(self):
        form = FormNewTask({
            'title': "Titulo test",
            'description': "Descripcion de test de titulo",
        })
        self.assertTrue(form.is_valid())
        post = form.save(commit=False)
        post.userTask = self.myuser1
        post.save()
        self.assertEqual(post.title, "Titulo test")
        self.assertEqual(post.description, "Descripcion de test de titulo")

    def test_blank_form_data(self):
        form = FormNewTask({})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'title': ['Este campo es requerido.'],
        })
    