# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import inspect

from task.models import InveraTask
from api.utils import send_test_csv_report

from django.contrib.auth.models import User
from rest_framework.test import APIClient, APITestCase
from rest_framework.reverse import reverse
from rest_framework import status

TEST_RESULTS = []
RECIPIENTS = ['email@destino.com']


class TaskListTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(
            username='test_user', password='adminpass')
        self.other_user = User.objects.create_user(
            username='other_user', password='adminpass')
        self.task = InveraTask.objects.create(
            userTask=self.user, title='My Initial Task')

        self.client = APIClient()

    @classmethod
    def tearDownClass(cls):
        User.objects.filter(username__in=['test_user', 'other_user']).delete()

    def test_create_task_with_un_authenticate_user(self):
        """
        En este caso de prueba, estamos probando la API Task Create utilizando un usuario no autenticado.
        """

        response = self.client.post(
            reverse('api-task'), {'title': 'My Task 1'}, format='json')

        is_passed = response.status_code == status.HTTP_403_FORBIDDEN

        TEST_RESULTS.append({
            "result": "Passed" if is_passed else "Failed",
            "test_name": inspect.currentframe().f_code.co_name,
            "test_description": "El usuario no autenticado no puede agregar una tarea a la lista"
        })

        if is_passed:
            print("Resultado: Aprobado")
        else:
            print("Resultado: Fallido")
        print("Nombre del test: " + inspect.currentframe().f_code.co_name)
        print("Descripcion: El usuario no autenticado no puede agregar una tarea a la lista")
        print("-----------")

    def test_put_task_with_un_authenticate_user(self):
        """
        En este caso de prueba, estamos probando la API Task PUT utilizando un usuario no autenticado.
        """

        response = self.client.put(
            reverse('api-task'), {'title': 'My Task'}, format='json')

        is_passed = response.status_code == status.HTTP_403_FORBIDDEN

        TEST_RESULTS.append({
            "result": "Passed" if is_passed else "Failed",
            "test_name": inspect.currentframe().f_code.co_name,
            "test_description": "El usuario no autenticado no puede modificar una tarea"
        })

        if is_passed:
            print("Resultado: Aprobado")
        else:
            print("Resultado: Fallido")
        print("Nombre del test: " + inspect.currentframe().f_code.co_name)
        print("Descripcion: El usuario no autenticado no puede modificar una tarea")
        print("-----------")

    def test_put_task_with_authenticated_user(self):
        self.client.login(username='test_user', password='adminpass')

        response = self.client.put(reverse('api-task-detail', args=[str(self.task.idTask)]), {'title': 'My Task 2'}, format='json')

        is_passed = response.status_code == status.HTTP_200_OK
        TEST_RESULTS.append({
            "result": "Passed" if is_passed else "Failed",
            "test_name": inspect.currentframe().f_code.co_name,
            "test_description": "Usuario autenticado puede modificar una tarea suya"
        })
        if is_passed:
            print("Resultado: Aprobado")
        else:
            print("Resultado: Fallido")
        print("Nombre del test: " + inspect.currentframe().f_code.co_name)
        print("Descripcion: Usuario autenticado puede modificar una tarea suya")
        print("-----------")
 

    def test_get_other_user_task_detail(self):
        """
        En este caso de prueba, estamos probando la API Task GET y tratando de obtener detalles de la tarea de un usuario que usa credenciales de usuario diferentes.
        """

        self.client.login(username='other_user', password='adminpass')

        response = self.client.get(reverse('api-task-detail', args=[str(self.task.idTask)]))

        is_passed = response.status_code == status.HTTP_404_NOT_FOUND

        # is_passed = response.status_code == status.HTTP_403_FORBIDDEN

        TEST_RESULTS.append({
            "result": "Passed" if is_passed else "Failed",
            "test_name": inspect.currentframe().f_code.co_name,
            "test_description": "Solo el propietario puede ver el detalle de la tarea"
        })
        if is_passed:
            print("Resultado: Aprobado")
        else:
            print("Resultado: Fallido")
        print("Nombre del test: " + inspect.currentframe().f_code.co_name)
        print("Descripcion: Solo el propietario puede ver el detalle de la tarea")
        print("-----------")
            
  

    def test_create_task_with_authenticated_user(self):
        self.client.login(username='test_user', password='adminpass')

        response = self.client.post(reverse('api-task'), {'title': 'My Task'}, format='json')

        is_passed = response.status_code == status.HTTP_201_CREATED
        TEST_RESULTS.append({
            "result": "Passed" if is_passed else "Failed",
            "test_name": inspect.currentframe().f_code.co_name,
            "test_description": "Usuario autenticado agrega tarea a la lista"
        })
        if is_passed:
            print("Resultado: Aprobado")
        else:
            print("Resultado: Fallido")
        print("Nombre del test: " + inspect.currentframe().f_code.co_name)
        print("Descripcion: Usuario autenticado agrega tarea a la lista")
        print("-----------")

    def test_get_task_detail(self):
        self.client.login(username='test_user', password='adminpass')

        response = self.client.get(reverse('api-task-detail', args=[str(self.task.idTask)]))

        is_passed = response.status_code == status.HTTP_200_OK

        TEST_RESULTS.append({
            "result": "Passed" if is_passed else "Failed",
            "test_name": inspect.currentframe().f_code.co_name,
            "test_description": "Usuario autenticado puede ver detalles de la tarea correctamente"
        })
        if is_passed:
            print("Resultado: Aprobado")
        else:
            print("Resultado: Fallido")
        print("Nombre del test: " + inspect.currentframe().f_code.co_name)
        print("Descripcion: Usuario autenticado puede ver detalles de la tarea correctamente")
        print("-----------")


class CSVReportTest(APITestCase):
    def test_send_csv(self):
        send_test_csv_report(
            test_results=TEST_RESULTS,
            recipients=RECIPIENTS
        )



