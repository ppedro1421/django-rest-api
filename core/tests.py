from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import *


class EmployerTest(APITestCase):
    def setUp(self):
        self.data = {'name': 'TESTS'}
        self.list = [
            {'name': 'TESTS 2'},
            {'name': 'TESTS 3'}
        ]

    def test_list_employer(self):
        [Employer.objects.create(**e) for e in self.list]
        response = self.client.get(reverse('employer-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_list_employer_empty(self):
        response = self.client.get(reverse('employer-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    def test_detail_employer(self):
        employer = Employer.objects.create(**self.data)
        response = self.client.get(reverse('employer-detail', args=[employer.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('name'), 'TESTS')

    def test_detail_employer_not_found(self):
        response = self.client.get(reverse('employer-detail', args=[1]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_employer(self):
        response = self.client.post(reverse('employer-create'), self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Employer.objects.count(), 1)
        self.assertEqual(Employer.objects.get().name, 'TESTS')

    def test_create_employer_error(self):
        response = self.client.post(reverse('employer-create'))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Employer.objects.count(), 0)


class RoleTest(APITestCase):
    def setUp(self):
        self.employer = Employer.objects.create(name='TEST')
        self.data = {'employer': self.employer, 'description': 'TESTER'}
        self.list = [
            {'employer': self.employer, 'description': 'TESTER 1'},
            {'employer': self.employer, 'description': 'TESTER 2'}
        ]

    def test_list_role(self):
        [Role.objects.create(**r) for r in self.list]
        response = self.client.get(reverse('role-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_list_role_empty(self):
        response = self.client.get(reverse('role-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    def test_create_role(self):
        response = self.client.post(reverse('role-create'), {**self.data, 'employer': self.employer.id})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Role.objects.count(), 1)
        self.assertEqual(Role.objects.get().description, 'TESTER')

    def test_create_role_error(self):
        response = self.client.post(reverse('role-create'))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Role.objects.count(), 0)


class ClientEmployeeTest(APITestCase):
    def setUp(self):
        self.employer = Employer.objects.create(name='TEST')
        self.role = Role.objects.create(employer=self.employer, description='TEST')
        self.data = {
            'employer': self.employer,
            'first_name': 'TEST E',
            'last_name': 'P',
            'role': self.role,
            'salary': 1234
        }
        self.list = [
            {
                'employer': self.employer,
                'first_name': 'TEST E',
                'last_name': 'P2',
                'role': self.role,
                'salary': 1234
            },
            {
                'employer': self.employer,
                'first_name': 'TEST E',
                'last_name': 'P3',
                'role': self.role,
                'salary': 1234
            }
        ]

    def test_list_employee(self):
        [Employee.objects.create(**e) for e in self.list]
        response = self.client.get(reverse('employee-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_list_employee_empty(self):
        response = self.client.get(reverse('employee-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    def test_detail_employee(self):
        employee = Employee.objects.create(**self.data)
        response = self.client.get(reverse('employee-detail', args=[employee.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('employer'), self.employer.id)

    def test_detail_employee_not_found(self):
        response = self.client.get(reverse('employee-detail', args=[1]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_employee(self):
        response = self.client.post(reverse('employee-create'), {**self.data, 'employer': self.employer.id, 'role': self.role.id})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Employee.objects.count(), 1)
        self.assertEqual(Employee.objects.get().employer, self.employer)

    def test_create_employee_error(self):
        response = self.client.post(reverse('employee-create'))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Employee.objects.count(), 0)
