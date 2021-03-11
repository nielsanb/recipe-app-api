from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

class AdminSiteTest(TestCase):
    #sometimes things need to be done before every test is ran.
    def setUp(self):
        #test client
        self.client = Client()

        #add user
        self.admin_user = get_user_model().objects.create_superuser(
            email='niels@niels.io',
            password='test123'
        )

        #login user into client
        self.client.force_login(self.admin_user)

        #regular user
        self.user = get_user_model().objects.create_user(
            email='niels2nd@niels.io',
            password='test1234',
            name='Test user full name'
        )

    def test_users_listed(self):
        """Test that users are listed on user page"""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)
        #checks that the response has an item in it.
        self.assertContains(res, self.user.name) 
        self.assertContains(res, self.user.email)

    def test_user_page_change(self):
        """Test that the user edit page works"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """Test that create user page works"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)