from django.test import TestCase
from accounts.models import PersonalAccount
from inscription.models import Affiliate, Scout

from datetime import datetime

class AfiliateTestCase(TestCase):

    def test_after_creation_personal_account_is_created(self):
        cantidad_de_personal_accounts = PersonalAccount.objects.count()
        new_affiliate = Scout.objects.create(name='nombre_del_afiliado', dni=12233424, birthday=datetime.now(), phone=123123123, adress='la_direccion', email='el_email')
        self.assertEqual(PersonalAccount.objects.count(), cantidad_de_personal_accounts+1)
        last_personal_accounts = PersonalAccount.objects.last()
        self.assertEqual(last_personal_accounts.name, str(new_affiliate.dni))
        self.assertEqual(last_personal_accounts.amount, 0)
        self.assertFalse(last_personal_accounts.inscription)
