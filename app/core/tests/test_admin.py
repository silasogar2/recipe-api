from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@gmail.com',
            password='pasword1234'
        )
        self.client.force_login(self.admin_user)
        self.users = get_user_model().objects.create_user(
            email='test@silasogar.tech',
            password='TestPass',
            name='Silas Ogar',
        )

    def test_users_listed(self):
        """Test if users are listed on users page"""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.users.name)
        self.assertContains(res, self.users.email)

    def test_user_change_page(self):
        """Test that the users edit page works"""
        url = reverse('admin:core_user_change', args=[self.users.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
