from django.test import TestCase
from django.urls import reverse
from accounts.models import Company, User
from .models import InboundShipment, OutboundShipment


class DashboardViewTest(TestCase):
    def setUp(self):
        self.company1 = Company.objects.create(name="Company A")
        self.company2 = Company.objects.create(name="Company B")
        self.user = User.objects.create_user(
            username="user1", password="pass", company=self.company1
        )
        InboundShipment.objects.create(
            company=self.company1,
            reference="IN1",
            status="Pending",
            expected_date="2023-01-01",
        )
        InboundShipment.objects.create(
            company=self.company2,
            reference="IN2",
            status="Pending",
            expected_date="2023-01-01",
        )
        OutboundShipment.objects.create(
            company=self.company1,
            reference="OUT1",
            status="Shipped",
            expected_date="2023-01-02",
        )
        OutboundShipment.objects.create(
            company=self.company2,
            reference="OUT2",
            status="Shipped",
            expected_date="2023-01-02",
        )

    def test_dashboard_shows_only_user_company_shipments(self):
        self.client.login(username="user1", password="pass")
        response = self.client.get(reverse('dashboard'))
        self.assertContains(response, "IN1")
        self.assertNotContains(response, "IN2")
        self.assertContains(response, "OUT1")
        self.assertNotContains(response, "OUT2")
