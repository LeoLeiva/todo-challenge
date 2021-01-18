from django.test import TestCase
import datetime
from task.models import InveraTask
from django.contrib.auth.models import User
from django.urls import reverse
from task.forms import FormNewTask

# Create your tests here.
class InveraTaskModelTest(TestCase):

    @classmethod
    def setUp(self):
        self.myuser1 = User.objects.create_user(username='Administrador 1', password='admin123', email='test@example.com')
        self.myuser2 = User.objects.create_user(username='Administrador 2', password='admin123', email='test1@test.com')
        dToday = datetime.date.today()
        Invera1 = InveraTask.objects.create(idTask=1, userTask=self.myuser1, title='Crear registro de usuarios', description='Crear registro con redes sociales',
            completed='False', created=dToday)
        Invera2 = InveraTask.objects.create(idTask=2, userTask=self.myuser2, title='Usar con docker', description='Terminar con docker',
            completed='True', created=dToday)
    
    def test_user(self):
        testTask1 = InveraTask.objects.get(idTask=1)
        testTask2 = InveraTask.objects.get(idTask=2)

        self.assertEquals(testTask1.userTask.username,'Administrador 1')
        self.assertEquals(testTask2.userTask.username,'Administrador 2')

    def test_title(self):
        testTask=InveraTask.objects.get(title="Crear registro de usuarios")
        self.assertEquals(testTask.title,'Crear registro de usuarios')

    def test_description(self):
        testTask=InveraTask.objects.get(description="Crear registro con redes sociales")
        self.assertEquals(testTask.description,'Crear registro con redes sociales')
    
    def test_completed(self):
        testTask=InveraTask.objects.get(completed=False)
        self.assertEquals(testTask.completed,False)

    def test_created(self):
        today = datetime.date.today()
        testTask=InveraTask.objects.get(idTask=1, created=today)
        self.assertEquals(testTask.created,today)

    #Si el usuario esta logueado devuelve 200
    def test_mytask_list_view_logued(self):
        self.client.login(username='Administrador 1', password='admin123')
        response = self.client.get(reverse('task'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Crear registro de usuarios')
        self.assertTemplateUsed(response, 'mytask.html')

    #Si el usuario no esta logueado redirecciona a formulario login
    def test_mytask_list_view(self):
        response = self.client.get(reverse('task'))
        self.assertEqual(response.status_code, 302)

    def test_title_max_length(self):
        testTask=InveraTask.objects.get(idTask=1)
        max_length = testTask._meta.get_field('title').max_length
        self.assertEquals(max_length,50)
