#from datetime import datetime
#
#from django.test import TestCase
#from accounts.models import Event, Budget, Items, Account, Movement
#from accounts.views import createMovement
#
#
## Create your tests here
#class AccountsTestCase(TestCase):
#
##    def setUp(self):
##        Event.objects.create(name="Locro", description="Una rica comida caliente para compartir en familia.", start="2006-01-01-16:30")
##        ev = Event.objects.last()
##        name_acc = ev.name + "_" + ev.id
##        Account.objects.create(name=name_acc, start=ev.start, wallet=0)
#
#    def test_account_created_have_amount_zero(self):
#        a = Account.objects.create(name='asdasd')
#        self.assertEqual(a.wallet, 0)
#
#
#
##    def test_bud_create_item(self):
#
#
#class MovementsTestCase(TestCase):
#    def setUp(self):
#        self.acc1 = Account.objects.create(name='account_A')
#        #self.acc2 = Account.objects.create(name='account_B')
#
#    def test_if_trying_to_move_fron_non_existent_Account_false_is_returned(self):
#        result = createMovement('name', 'desc', None, 5, 0, 'asd', False)
#        self.assertFalse(result)
#        self.assertFalse(createMovement('name', 'desc', None, 5, self.acc1.id, 'asd', False))
#        self.assertFalse(createMovement('name', 'desc', None, 5, 0, self.acc1.name, False))
#        self.assertEqual(self.acc1.wallet, 0)
#
#    def test_success_updates_account_wallet(self):
#        m_n = 'mov name'
#        m_desc = 'mov description'
#        m_date = datetime.now()
#        ammount = 7
#        stat = True
#        result = createMovement(m_n, m_desc, m_date, ammount, self.acc1.id,
#                               self.acc1.name, stat)
#        self.assertTrue(result)
#        updated_account = Account.objects.get(id=self.acc1.id)
#        self.assertEqual(updated_account.wallet, ammount)
#
#
#    def test_success_creates_movement(self):
#        m_n = 'mov name'
#        m_desc = 'mov description'
#        m_date = datetime.now()
#        ammount = 7
#        stat = True
#        result = createMovement(m_n, m_desc, m_date, ammount, self.acc1.id,
#                               self.acc1.name, stat)
#        self.assertTrue(result)
#        self.assertEqual(Movement.objects.count(), 1)
#        last_m = Movement.objects.last()
#        self.assertEqual(last_m.amount, ammount)
#        self.assertEqual(last_m.name, m_n)
#
#class EventTestCase(TestCase):
#
#    def test_after_creation_account_is_created(self):
#        return
#        self.assertEqual(Account.objects.count(), 0)
#        e = Event.objects.create(name='Locro')
#        self.assertEqual(Accounts.objects.count(), 1)
#        acc = Accounts.objects.last()
#        self.assertEqual(acc.name, e.name + '_' + str(e.id))
#        self.assertEqual(acc.start, e.start)
