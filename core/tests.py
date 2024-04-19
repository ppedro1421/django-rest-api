from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import *


class ClientTest(APITestCase):
    def setUp(self):
        self.data = {'name': 'TESTS', 'cnpj': '00.503.484/0001-91'}
        self.list = [
            {'name': 'TESTS 2', 'cnpj': '12.123.123/0001-12'},
            {'name': 'TESTS 3', 'cnpj': '23.234.234/0001-23'}
        ]

    def test_list_client(self):
        [Client.objects.create(**c) for c in self.list]
        response = self.client.get(reverse('client-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_list_client_empty(self):
        response = self.client.get(reverse('client-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    def test_detail_client(self):
        client = Client.objects.create(**self.data)
        response = self.client.get(reverse('client-detail', args=[client.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('name'), 'TESTS')

    def test_detail_client_not_found(self):
        response = self.client.get(reverse('client-detail', args=[1]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_client(self):
        response = self.client.post(reverse('client-create'), self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Client.objects.count(), 1)
        self.assertEqual(Client.objects.get().name, 'TESTS')

    def test_create_client_error(self):
        response = self.client.post(reverse('client-create'))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Client.objects.count(), 0)


class ClientEmployeeTest(APITestCase):
    def setUp(self):
        self.employer = Client.objects.create(name='TEST', cnpj='12.123.123/0001-12')
        self.data = {
            'employer': self.employer,
            'first_name': 'TEST E',
            'last_name': 'P',
            'cpf': '111.111.111-11',
            'role': 'TEST',
            'salary': 1234
        }
        self.list = [
            {
                'employer': self.employer,
                'first_name': 'TEST E',
                'last_name': 'P2',
                'cpf': '222.222.222-22',
                'role': 'TEST',
                'salary': 1234
            },
            {
                'employer': self.employer,
                'first_name': 'TEST E',
                'last_name': 'P3',
                'cpf': '333.333.333-33',
                'role': 'TEST',
                'salary': 1234
            }
        ]

    def test_list_employee(self):
        [ClientEmployee.objects.create(**e) for e in self.list]
        response = self.client.get(reverse('employee-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_list_employee_empty(self):
        response = self.client.get(reverse('employee-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    def test_detail_employee(self):
        employee = ClientEmployee.objects.create(**self.data)
        response = self.client.get(reverse('employee-detail', args=[employee.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('employer'), self.employer.id)

    def test_detail_employee_not_found(self):
        response = self.client.get(reverse('employee-detail', args=[1]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_employee(self):
        response = self.client.post(reverse('employee-create'), {**self.data, 'employer': self.employer.id})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ClientEmployee.objects.count(), 1)
        self.assertEqual(ClientEmployee.objects.get().employer, self.employer)

    def test_create_employee_error(self):
        response = self.client.post(reverse('employee-create'))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(ClientEmployee.objects.count(), 0)
