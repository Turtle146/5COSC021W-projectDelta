from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Department, Team, Dependency

class DepartmentViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser', password='testpass123'
        )
        self.dept = Department.objects.create(
            department_name='Test Department',
            department_description='A test department'
        )

    def test_department_list_redirects_if_not_logged_in(self):
        response = self.client.get('/departments/')
        self.assertEqual(response.status_code, 302)

    def test_department_list_loads_when_logged_in(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get('/departments/')
        self.assertEqual(response.status_code, 200)

    def test_department_detail_loads(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(f'/departments/{self.dept.id}/')
        self.assertEqual(response.status_code, 200)

    def test_department_search(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get('/departments/?q=Test')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Department')

    def test_organisation_view_loads(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get('/organisation/')
        self.assertEqual(response.status_code, 200)


class TeamViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser', password='testpass123'
        )
        self.dept = Department.objects.create(
            department_name='Test Department'
        )
        self.team = Team.objects.create(
            team_name='Test Team',
            department=self.dept,
            mission='Test mission'
        )

    def test_team_detail_loads(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(f'/teams/{self.team.id}/')
        self.assertEqual(response.status_code, 200)

    def test_team_detail_redirects_if_not_logged_in(self):
        response = self.client.get(f'/teams/{self.team.id}/')
        self.assertEqual(response.status_code, 302)


class ModelTests(TestCase):

    def test_department_str(self):
        dept = Department.objects.create(department_name='xTV_Web')
        self.assertEqual(str(dept), 'xTV_Web')

    def test_team_str(self):
        dept = Department.objects.create(department_name='xTV_Web')
        team = Team.objects.create(team_name='Code Warriors', department=dept)
        self.assertEqual(str(team), 'Code Warriors')