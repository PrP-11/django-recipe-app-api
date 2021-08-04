from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@prp.com',
            password='secret@123'
        )

        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='test@prp.com',
            password='secret@123',
            name='Test user full name'
        )
    

    def test_users_listed(self):
        """Test that users are listed on user page"""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        # This also tests for http status 200 and that looks for content in res
        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    