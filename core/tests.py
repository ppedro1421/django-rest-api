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

    def test_get_employer(self):
        employer = Employer.objects.create(**self.data)
        response = self.client.get(reverse('employer-get', args=[employer.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('name'), 'TESTS')

    def test_get_employer_not_found(self):
        response = self.client.get(reverse('employer-get', args=[uuid.uuid4()]))
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

    def test_update_employer(self):
        employer = Employer.objects.create(**self.data)
        response = self.client.put(reverse('employer-update', args=[employer.id]), {
            'name': 'Updated'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Employer.objects.get().name, 'Updated')


class ClientEmployeeTest(APITestCase):
    def setUp(self):
        self.employer = Employer.objects.create(name='TEST')
        self.data = {
            'employer': self.employer,
            'first_name': 'TEST E',
            'last_name': 'P',
            'role': 'DEV',
            'salary': 1234
        }
        self.list = [
            {
                'employer': self.employer,
                'first_name': 'TEST E',
                'last_name': 'P2',
                'role': 'DEV',
                'salary': 1234
            },
            {
                'employer': self.employer,
                'first_name': 'TEST E',
                'last_name': 'P3',
                'role': 'DEV',
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

    def test_get_employee(self):
        employee = Employee.objects.create(**self.data)
        response = self.client.get(reverse('employee-get', args=[employee.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('employer'), self.employer.id)

    def test_get_employee_not_found(self):
        response = self.client.get(reverse('employee-get', args=[uuid.uuid4()]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_employee(self):
        response = self.client.post(reverse('employee-create'), {
            **self.data,
            'employer': self.employer.id,
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Employee.objects.count(), 1)
        self.assertEqual(Employee.objects.get().employer, self.employer)

    def test_create_employee_error(self):
        response = self.client.post(reverse('employee-create'))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Employee.objects.count(), 0)

    def test_update_employee(self):
        employee = Employee.objects.create(**self.data)
        response = self.client.put(reverse('employee-update', args=[employee.id]), {
            **self.data, 
            'employer': self.employer.id, 
            'first_name': 'Updated'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Employee.objects.get().first_name, 'Updated')
